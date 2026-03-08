from flask import Flask
import subprocess

app = Flask(__name__)

@app.route("/")
def home():
    return "Face Detection Backend Running"

@app.route("/start")
def start():
    subprocess.Popen(["python", "facedetection.py"], cwd="backend")
    return "Detection Started"

if __name__ == "__main__":
    app.run(debug=True)