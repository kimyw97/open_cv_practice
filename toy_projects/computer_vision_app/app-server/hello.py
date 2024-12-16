from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO, emit
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import numpy as np
import cv2
import base64
import mediapipe as mp

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins='*')
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({"error": "No image file provided"}), 400
    
    file = request.files['image']
    filter_type = request.form.get('filter','gray')

    try:
        image_stream = file.read()
        converted_img = np.frombuffer(image_stream, np.uint8)
        result_img = apply_filter(converted_img, filter_type)

        return result_img, 200, {'Content-Type': 'image/jpeg'}
    except Exception as e:
        return jsonify({'err': str(e)},500)

def apply_filter(converted_img, filter_type):
    img = cv2.imdecode(converted_img, cv2.IMREAD_COLOR)

    if filter_type == 'gray':
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    elif filter_type == 'blur':
        img = cv2.GaussianBlur(img, (15, 15), 0)
    elif filter_type == 'edges':
        img = cv2.Canny(img, 100, 200)
    elif filter_type == 'sepia':
        sepia_filter = np.array([[0.272, 0.534, 0.131],
                                 [0.349, 0.686, 0.168],
                                 [0.393, 0.769, 0.189]])
        img = cv2.transform(img, sepia_filter)
    elif filter_type == 'brightness':
        brightness = 50
        img = cv2.convertScaleAbs(img, beta=brightness)
    elif filter_type == 'contrast':
        contrast = 1.5
        img = cv2.convertScaleAbs(img, alpha=contrast)

    _, buffer = cv2.imencode('.jpeg', img)
    img_stream = buffer.tobytes()
    return img_stream

@app.route('/mosaic', methods=['Post'])
def mosaic():
    if 'image' not in request.files:
        return jsonify({'error': 'No Image'}), 400
    file = request.files['image']
    mosaic_method = request.form.get('mosaicMethod', 'resize')

    stream = file.read()
    converted_img = np.frombuffer(stream, np.uint8)

    img = cv2.imdecode(converted_img, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x,y,w,h) in faces:
        mosaic_level = 10
        face = img[y:y+h, x:x+w]
        if mosaic_method == 'resize':
            small_face = cv2.resize(face, (w// mosaic_level, h//mosaic_level), interpolation=cv2.INTER_LINEAR)
            face = cv2.resize(small_face, (w,h), interpolation=cv2.INTER_LINEAR)
        elif mosaic_method == 'blur':
            face = cv2.blur(face, (7,7), anchor=(-1,-1), borderType=cv2.BORDER_DEFAULT)
        elif mosaic_method == 'gaussian':
            face = cv2.GaussianBlur(face, (7,7), 0)
        img[y:y+h, x:x+w] = face
    _,buffer =cv2.imencode('.jpeg',img)
    img_stream = buffer.tobytes()

    return img_stream, 200, {'Content-Type': 'image/jpeg'}

@socketio.on('send_frame')
def handle_frame(data):
    img_data = base64.b64decode(data['frame'])
    np_img = np.frombuffer(img_data, np.uint8)
    img = cv2.imdecode(np_img, cv2.IMREAD_COLOR)
    img = resize_image(img)

    # STEP 2: Create an HandLandmarker object.
    base_options = python.BaseOptions(model_asset_path='./app-server/hand_landmarker.task')
    options = vision.HandLandmarkerOptions(base_options=base_options,
                                       num_hands=2)
    detector = vision.HandLandmarker.create_from_options(options)

    # STEP 3: Load the input image.
    image = mp.Image(image_format=mp.ImageFormat.SRGB, data=img)

    # STEP 4: Detect hand landmarks from the input image.
    detection_result = detector.detect(image)

    # STEP 5: Process the classification result. In this case, visualize it.
    annotated_image = draw_landmarks_on_image(image.numpy_view(), detection_result)

    _, buffer = cv2.imencode('.jpg',annotated_image)
    frame_b64 = base64.b64encode(buffer).decode('utf-8')


    socketio.emit('receive_frame', {'frame': frame_b64})

def draw_landmarks_on_image(image,detection_result):
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    for hand_landmarks in detection_result.hand_landmarks:
        for landmark in hand_landmarks:
            x = int(landmark.x * image.shape[1])
            y = int(landmark.y * image.shape[0])
            cv2.circle(image, (x,y), 5, (0,255,0),-1)
    return image

def resize_image(image, max_width=1024, max_height=1024):
    height, width = image.shape[:2]
    if width > max_width or height > max_height:
        scaling_factor = min(max_width / width, max_height / height)
        new_width = int(width * scaling_factor)
        new_height = int(height * scaling_factor)
        image = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_AREA)
    return image

if __name__ == '__main__':
    try:
        app.run('0.0.0.0', port=4000, debug=True)
    except Exception as e:
        print(f'err: {e}')
