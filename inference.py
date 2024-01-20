import os 
import subprocess
from PIL import Image

yolov7 = "yolov7/detect.py"
model_weigths = "best.pt"
input_image = "images/inference_img.jpg"