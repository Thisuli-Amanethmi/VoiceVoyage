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


def generate_frames():
    # Capture video frames and perform object detection
    cap = cv2.VideoCapture(0)  # Use default camera

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break

        detect_params = model.predict(source=[frame], conf=0.6, save=False)
        DP = detect_params[0].numpy()

        if len(DP) != 0:
            detected_classes = []
            for i in range(len(detect_params[0])):
                # ... (Object detection and rendering logic, same as provided code)

                # Navigation announcement
                announcement = yolo8_custom_live.navigation_algo_part2(Current_object_list, Previous_object_list)
                print(Previous_object_list)
                engine.say(announcement)
                engine.runAndWait()
                Current_object_list = []

        # Encode frame as JPEG for response
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route("/start_detection")
def start_detection():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route("/stop_detection")
def stop_detection():
    global cap  # Access the global variable
    cap.release()
    return "Detection Stopped"


if __name__ == "__main__":
    app.run(debug=True)  # Set debug=False for production
