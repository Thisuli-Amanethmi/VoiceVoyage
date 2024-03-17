from flask import Flask, render_template, Response, request
import cv2
import numpy as np
import random
from threading import Thread
import time
import pyttsx3 
from pyttsx3 import init # Import for text-to-speech
from ultralytics import YOLO  # Assuming you have ultralytics installed


# Define class list and colors (modify as needed)
class_list = [
    "bed", "bookshelf", "chair", "clothes-rack", "coffee-table", "commode",
    "cupboard", "door", "dressing-table", "lamp", "oven", "pantry-cupboards",
    "refrigerator", "shoe-rack", "sink", "sofa", "staircase", "stove", "table",
    "tv", "wall-art", "washing-machine", "window"
]

# Generate random colors for each class
detection_colors = [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for _ in range(len(class_list))]

# Load YOLOv8 model (replace with your model path)
model = YOLO("voiceVoyage_version8_best.pt", "v8")  # Assuming correct path

# Initialize text-to-speech engine
engine = init()

# Set video resolution (adjust as needed)
frame_width = 640
frame_height = 480

# Global variables (consider using thread-safe alternatives)
detected_objects = []
announcement = ""
previous_objects = []  # Assuming no initial objects


def generate_frames():
    global detected_objects, announcement, previous_objects
    cap = cv2.VideoCapture(0)  # Change to video file path if needed

    if not cap.isOpened():
        print("Error opening camera")
        return

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Can't receive frame (stream end?). Exiting...")
            break

        # Resize frame (optional, adjust based on performance requirements)
        # frame = cv2.resize(frame, (frame_width, frame_height))

        # Perform object detection with YOLO
        print(type(results))
        print(results)
        results = model(frame)
        results.render()  # Render detections (optional)

        # Process detections
        detected_objects.clear()
        for result in results.pandas().xyxy[0]:  # Assuming single image output
            conf = round(result["confidence"], 3)
            if conf > 0.6:  # Adjust confidence threshold as needed
                cls = class_list[int(result["class"])]
                detected_objects.append(cls)

        # Navigation algorithm (assuming implementation is available)
        # if NV and DB are imported:
        #     announcement = navigation_algo_part2(detected_objects, previous_objects)
        # else:
        #     print("Navigation algorithm not implemented")
        announcement = "Object detection and navigation algorithm not yet implemented."

        # Announce detected objects (replace with your logic)
        if detected_objects:
            if type(detected_objects) == list:
                for obj in detected_objects:
                    engine.say(obj)
                    engine.runAndWait()
            else:
                engine.say(detected_objects)
                engine.runAndWait()

        previous_objects = detected_objects.copy()  # Update previous objects

        # Convert frame to bytes for streaming
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

        time.sleep(0.1)  # Adjust delay between frames as needed

    cap.release()
    cv2.destroyAllWindows()


app = Flask(__name__)


@app.route('/')
def video():
    return render_template('index.html')  # Replace with your template


@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)
