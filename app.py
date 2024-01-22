from flask import Flask, render_template, request, jsonify
import os 
import subprocess
from PIL import Image
app = Flask(__name__)

yolov7 = "yolov7/detect.py"
model_weigths = "best.pt"
save_result = "results"
conf = 0.4
img_path = 'images/infer.jpg'

detect = [
    'python', yolov7,
    '--weights', model_weigths,
    '--img-size', '512',
    '--conf', str(conf),
    '--source', img_path,
    '--save-txt',
    '--save-conf',
    '--project', save_result,
    '--no-trace',
    '--exist-ok',
]

preprocess = [
    'python3', 'preprocess.py',
    '--input', img_path,
    '--output', img_path,
    
]

@app.route('/', methods = ['GET'])
def index():
    return render_template('index.html')

@app.route('/upload', methods = ['POST'])
def upload():
    img = request.files['file']
    img.save(img_path)
    subprocess.run(preprocess)
    subprocess.run(detect)

if __name__ == '__main__':
    app.run(debug=True)
    