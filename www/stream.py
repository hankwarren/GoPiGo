#!/usr/bin/venv python
from flask import Flask, render_template, Response
from camera import PiCamera

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html"')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b '--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Rsponse(gen(Camera()),
                mimetype='multipart/x-mixed-replace; bounder=frame')