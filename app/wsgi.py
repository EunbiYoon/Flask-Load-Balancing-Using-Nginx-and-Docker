from flask import Flask
import socket

app = Flask(__name__)

@app.route("/")
def hello():
    return f"Container ID : {socket.gethostname()}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)