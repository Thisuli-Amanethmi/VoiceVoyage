from OntologyGraph import Database as DB, NavAlgo as NV

import numpy as np
import cv2
from ultralytics import YOLO
import random
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def Navigation_algorithm(current_object_list,previous_object_list):
    left=0
    right=0
    index=0
    midIndex=0
    left_obj=[NV.queryLeft,NV.queryFarLeft]
    right_obj=[NV.queryRight,NV.queryFarRight]
    mid_obj=[NV.front,NV.queryCenter]
    if (previous_object_list[-1] in left_obj and (i in left_obj for i in current_object_list)) or (previous_object_list[-1] in mid_obj and (i in left_obj for i in current_object_list) ):
        announcement="You are in the left side if the room."
    elif (previous_object_list[-1] in right_obj and (i in right_obj for i in current_object_list)) or (previous_object_list[-1] in mid_obj and (i in right_obj for i in current_object_list)):
        announcement = "You are in the right side if the room."
    for i in current_object_list:
        if i in left_obj:
            left+=1
        elif i in right_obj:
            right+=1
    if (NV.queryFarLeft in previous_object_list) and (( NV.queryLeft) in current_object_list):
        announcement=NV.queryLeft+" is in your front."
    elif (NV.queryLeft in previous_object_list):
        if (NV.queryCenter in current_object_list):
            announcement =NV.queryCenter+" is in your right."
        elif NV.front in current_object_list:
            announcement=NV.queryCenter +" is in your left."



    if left>0:
        for i in current_object_list:
            if i in left_obj:
                idex=i
            elif i in mid_obj:
                midIndex=i
        announcement1=current_object_list[idex]+" in your left."
        if midIndex!=0:
            announcement2=current_object_list[midIndex]+" is in your right."
    elif right>0:
        for i in current_object_list:
            if i in right_obj:
                idex=i
            elif i in mid_obj:
                midIndex=i
        announcement=current_object_list[idex]+" in your right."
        if midIndex!=0:
            announcement2=current_object_list[midIndex]+" is in your right."











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





