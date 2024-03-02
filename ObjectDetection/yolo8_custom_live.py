from OntologyGraph import Database as DB, NavAlgo as NV

import numpy as np
import cv2
from ultralytics import YOLO
import random
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def Navigation_algorithm(object,detected_list):
    if len(detected_list)<=2 and object==NV.front:
        announcement = "The "+object+" infront of you."
    if len(detected_list<5) and (object not in detected_list) and object==NV.queryLeft:
        announcement=""

class_list = ["bed","bookshelf","chair","clothes-rack","coffee-table","commode","cupboard","door","dressing-table","lamp","oven","pantry-cupboards","refrigerator","shoe-rack","sink","sofa","staircase","stove","table","tv","wall-art","washing-machine","window"]


# print(class_list)

# Generate random colors for class list
detection_colors = []
for i in range(len(class_list)):
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    detection_colors.append((b,g,r))

# load a pretrained YOLOv8n model
model = YOLO("voiceVoyage_version8_best.pt", "v8")

# Vals to resize video frames | small frame optimise the run
frame_wid = 640
frame_hyt = 480

# cap = cv2.VideoCapture(1)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True

    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # resize the frame | small frame optimise the run.
    #frame = cv2.resize(frame, (frame_wid, frame_hyt))

    # Predict on image
    detect_params = model.predict(source=[frame], conf=0.45, save=False)


    # Convert tensor array to numpy
    DP = detect_params[0].numpy()


    if len(DP) != 0:
        detected_classes = []
        for i in range(len(detect_params[0])):
            boxes = detect_params[0].boxes
            box = boxes[i]  # returns one box
            clsID = box.cls.numpy()[0]
            conf = box.conf.numpy()[0]
            bb = box.xyxy.numpy()[0]


            cv2.rectangle(
                frame,
                (int(bb[0]), int(bb[1])),
                (int(bb[2]), int(bb[3])),
                detection_colors[int(clsID)],
                3,
            )


            # Display class name and confidence
            font = cv2.FONT_HERSHEY_COMPLEX
            cv2.putText(
                frame,
                class_list[int(clsID)]
                + " "
                + str(round(conf, 3))
                + "%",
                (int(bb[0]), int(bb[1]) - 10),
                font,
                1,
                (255, 255, 255),
                2,
            )
            # Collect detected classes for speech
            if class_list[int(clsID)] not in detected_classes:
                detected_classes.append(class_list[int(clsID)])



            # Announce detected objects if any
            if detected_classes:
                announcement = "Detected " + ", ".join(detected_classes)
                engine.say(announcement)
                engine.runAndWait()

    # Display the resulting frame
    cv2.imshow('ObjectDetection', frame)

    # Terminate run when "Q" pressed
    if cv2.waitKey(1) == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()





