from PIL import Image
import argparse

def preprocess_image(INPUT_PATH, OUTPUT_PATH):
    image = Image.open(INPUT_PATH)
    image = image.resize((512,512)).convert('L')
    image.save(OUTPUT_PATH)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'preprocess image for object detection')
    parser.add_argument('--input', help='input path of the file')
    parser.add_argument('--output', help = 'output path of the file')
    args = parser.parse_args()
    preprocess_image(args.input, args.output)