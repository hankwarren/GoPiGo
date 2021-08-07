from flask import Flask, Response
from picamera import PiCamera

import gopigo

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/forward')
def forward():
    gopigo.fwd()
    return 'forward'

@app.route('/backward')
def backward():
    gopigo.bwd()
    return 'backward'

@app.route('/left')
def left():
    gopigo.left()
    return 'left'

@app.route('/right')
def right():
    gopigo.right()
    return 'right'

@app.route('/stop')
def stop():
    gopigo.stop()
    return 'stop'

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(PiCamera()),
            mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(debug = True, host='0.0.0.0', port=5000)
