from flask import Flask, render_template, Response
import cv2
from ultralytics import YOLO
import random
import pyttsx3
from io import BytesIO

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Object class list
class_list = [
    "bed", "bookshelf", "chair", "clothes-rack", "coffee-table", "commode", "cupboard", "door", "dressing-table", "lamp", "oven", "pantry-cupboards",
    "refrigerator", "shoe-rack", "sink", "sofa", "staircase", "stove", "table", "tv", "wall-art", "washing-machine", "window"
]

# Generate random colors for class list
detection_colors = []
for i in range(len(class_list)):
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)
  detection_colors.append((b, g, r))

# Load YOLO model (replace with your model path)
model = YOLO("voiceVoyage_version8_best.pt")

# Define helper functions
def generate_announcement(detected_classes):
  announcement = ""
  if detected_classes:
    for i in detected_classes:
      announcement += i + " "
  else:
    announcement = "No objects detected."
  return announcement

def draw_detections(frame, boxes, confidences, class_ids):
  for i in range(len(boxes)):
    # Extract bounding box coordinates and confidence score
    x_min, y_min, x_max, y_max = boxes[i]
    confidence = confidences[i]
    class_id = class_ids[i]

    # Draw rectangle around detected object
    cv2.rectangle(frame, (int(x_min), int(y_min)), (int(x_max), int(y_max)), detection_colors[class_id], 2)

    # Display class name and confidence score
    font = cv2.FONT_HERSHEY_COMPLEX
    cv2.putText(frame, f"{class_list[class_id]} {confidence:.2f}", (int(x_min), int(y_min) - 10), font, 0.7, (255, 255, 255), 2)

def process_frame(frame):
  # Resize frame (optional, adjust dimensions as needed)
  # frame = cv2.resize(frame, (640, 480))

  # Perform object detection with YOLO
  results = model.predict(source=[frame], conf=0.6, save=False)[0]

  # Extract detected objects and their properties
  boxes = results.boxes.numpy()
  confidences = results.scores.numpy()
  class_ids = results.classes.numpy()

  # Draw detections on the frame
  draw_detections(frame, boxes, confidences, class_ids)

  # Collect detected classes for announcement
  detected_classes = []
  for i in range(len(boxes)):
    detected_classes.append(class_list[class_ids[i]])

  # Generate announcement text
  announcement = generate_announcement(detected_classes)
  engine.say(announcement)
  engine.runAndWait()

  return frame, announcement

# Flask app setup
app = Flask(__name__)

@app.route('/video')
def video():
  # Access camera
  cap = cv2.VideoCapture(0)

  def generate():
    while True:
      ret, frame = cap.read()
      if not ret:
        print("Can't receive frame, exiting...")
        break

      # Process frame for object detection and announcement
      processed_frame, announcement = process_frame(frame)

      # Convert frame to bytes for streaming
      _, buffer = cv2.imencode('.jpg', processed_frame)
      frame_bytes = buffer.tobytes()

      # Set announcement as response header
      yield (b'--frame\r\n'
             b'Content-Type: image/jpeg\r\n'
             b'X-Announcement: ' + announcement.encode('utf-8') + b'\r\n\r\n' + frame_bytes + b'\r\n')

  return Response(generate(), mimetype='multipart/x-mixed-replace; boundary=frame')
