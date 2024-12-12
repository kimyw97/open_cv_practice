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
    if 'image' not in request.files:# explain this line
        return jsonify({"error": "No image file provided"}), 400
    
    file = request.files['image']

    try:
        image_stream = file.read()
        converted_img = np.frombuffer(image_stream, np.uint8)
        img = cv2.imdecode(converted_img, cv2.IMREAD_COLOR)

        gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        _, buffer = cv2.imencode('.jpeg', gray_img)
        gray_img_stream = buffer.tobytes()

        return gray_img_stream, 200, {'Content-Type': 'image/jpeg'}
    except Exception as e:
        return jsonify({'err': str(e)},500)

if __name__ == '__main__':
    app.run('0.0.0.0', port=4000, debug=True)
