from flask import Flask, request, jsonify
import numpy as np
import cv2
from flask_cors import CORS
app = Flask(__name__)
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

if __name__ == '__main__':
    try:
        app.run('0.0.0.0', port=4000, debug=True)
    except Exception as e:
        print(f'err: {e}')
