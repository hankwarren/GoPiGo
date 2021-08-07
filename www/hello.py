from flask import Flask
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

if __name__ == "__main__":
    app.run(debug = True, host='0.0.0.0', port=5000)
