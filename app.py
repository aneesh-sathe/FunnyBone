from flask import Flask, render_template, request, jsonify, send_from_directory
import os 
from langchain_community.llms import ollama
import math
import subprocess
from PIL import Image
app = Flask(__name__)

yolov7 = "yolov7/detect.py"
model_weigths = "best.pt"
save_result = "results"
conf = 0.4
img_path = 'images/infer.jpg'

# class look-up table 
class_table = ['elbow positive', 'fingers positive', 'forearm fracture', 'humerus fracture', 'shoulder fracture', 'wrist positive']

#llm = ollama(model='llama2')

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

    if os.listdir('results/exp/labels'): # delete previous result labels
        os.remove('results/exp/labels/infer.txt')
    
    subprocess.run(preprocess)
    subprocess.run(detect)
    
    if os.listdir('results/exp/labels'):
        with open('results/exp/labels/infer.txt', 'r') as result_file:
            res, conf = result_file.readlines()[-1].split()[::5]
            result = {
                "condition" : class_table[int(res)],
                "confidence" : math.floor(float(conf)*100),
            }
    else:
        result = {
            "condition" : "unable to detect fracture, consult a doctor!",
            "confidence" : "N/A"
        }
        
    return render_template('result.html', result = result)
        
@app.route('/result_image')
def result_image():
    return send_from_directory('results/exp', 'infer.jpg')

if __name__ == '__main__':
    app.run(debug=True)
    