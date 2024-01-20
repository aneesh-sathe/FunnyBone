from flask import Flask, render_template, request, jsonify
save_path = 'images'
app = Flask(__name__)

@app.route('/', methods = ['GET'])
def index():
    return "<h1>Hello, World!</h1>"

@app.route('/upload', methods = ['POST'])
def upload():
    img = request.files['file']
    img.save(save_path)
    
    

if __name__ == '__main__':
    app.run(debug=True)
    