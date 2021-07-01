from flask import Flask, render_template, request, Response, redirect, url_for
from PIL import Image

import os

from eval import captionize
from utils import *

app = Flask(__name__)

img_name = "1.jpg"
#input_path = r"/home/xori/github/hackathons/Hackfest-IIT-ISM-Dhanbad-2021-/static/a.jpg"
#output_path = r"/home/xori/github/hackathons/Hackfest-IIT-ISM-Dhanbad-2021-/static/output.mp3"
output_path = r"C:\Users\Desktop\NST\OBJECT_DETECTION\ouput.mp3"
input_path=r"C:\Users\Desktop\TEST_IMAGES\1.jpg"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api', methods=['GET', 'POST'])
def api():
    if(request.method == 'POST'):
        f = request.files['img']
        f.save("static/a.jpg")
        img=cv2.imread(input_path)
        img = Image.fromarray(img)
        captionize(img, output_path, play_now=False,print_caption=True)

        return render_template('result.html')

if __name__ == "__main__":
    app.run(debug=True)