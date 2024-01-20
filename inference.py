import os 
import subprocess
from PIL import Image

yolov7 = "yolov7/detect.py"
model_weigths = "best.pt"
input_image = "images/inference_img.jpg"
save_result = "results"
conf = 0.4

detect = [
    'python', yolov7,
    '--weights', model_weigths,
    '--img-size', '512',
    '--conf', str(conf),
    '--source', input_image,
    '--save-txt',
    '--save-conf',
    '--project', save_result,
    '--no-trace',
    '--exist-ok',
]

subprocess.run(detect)
