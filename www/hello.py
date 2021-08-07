from flask import Flask
import gopigo

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/forward')
def forward():
    gopigo.fwd()

@app.route('/backward')
def backward():
    gopigo.bwd()

@app.route('/left')
def left():
    gopigo.left()

@app.route('/right')
def right():
    gopigo.right()

@app.route('/stop')
def stop():
    gopigo.stop()


if __name__ == "__main__":
    app.run(debug = True, host='0.0.0.0', port=5000)
