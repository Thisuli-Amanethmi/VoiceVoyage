from flask import Flask, render_template, Response
import numpy as np
import cv2
from ultralytics import YOLO
import random
import pyttsx3

from ObjectDetection import yolo8_custom_live

# Initialize Flask app and text-to-speech engine
app = Flask(__name__)
engine = pyttsx3.init()

# Global variables for object tracking
Previous_object_list = []
Current_object_list = []

# Load YOLOv8 model
model = YOLO("voiceVoyage_version8_best.pt", "v8")


@app.route("/")
def index():
    return render_template("index.html")  # Assuming a basic HTML template

def main():
    yolo8_custom_live.main()
    

@app.route("/start_detection")
def start_detection():
    return Response(main(), mimetype='multipart/x-mixed-replace; boundary=frame')
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route("/stop_detection")
def stop_detection():
    global cap  # Access the global variable
    cap.release()
    return "Detection Stopped"


if __name__ == "__main__":
    app.run(debug=True)  # Set debug=False for production
