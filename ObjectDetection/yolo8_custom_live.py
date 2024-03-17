from OntologyGraph import Database as DB, NavAlgo as NV

import numpy as np
import cv2
from ultralytics import YOLO
import random
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()
Previous_object_list=[]
Current_object_list=[]

def Navigation_algorithm(object_list):
    left=0
    right=0
    mid=0
    Left_obj=[NV.queryLeft,NV.queryFarLeft]
    Right_obj=[NV.Right,NV.queryFarRight]
    Mid_obj=[NV.queryCenter,NV.front]

    for index in object_list:
        if index in Left_obj:
            left+=1
            Left_object =object_list.index(index)
        elif index in Right_obj:
            right+=1
            Right_object = object_list.index(index)
        elif index in Mid_obj:
            mid+=1
            Mid_object =object_list.index(index)

    if left>right and left>mid:
        return "Left", Left_object
    elif right>left and right>mid:
        return "Right", Right_object
    elif mid>right and mid>left:
        return "mid", Mid_object
    else:
        return 0,0


def CheckForTurnBack(Current_object_list, Previous_object_list):
    if (len(Current_object_list) >= 2 and len(Previous_object_list) >= 2):
        if(Current_object_list[-1] == Previous_object_list[-1] and Current_object_list[-2] == Previous_object_list[-2]):
            TurnBackDetected = True
            return TurnBackDetected

        else:
            TurnBackDetected = False
            return TurnBackDetected
    else:
        TurnBackDetected = False
        return TurnBackDetected


def navigation_algo_part2(Current_object_list,Previous_object_List):
    Current_orientation, Current_object_index = Navigation_algorithm(Current_object_list)
    Previous_orientation, Previous_object_index = Navigation_algorithm([Previous_object_List[-1]])
    TurnBackDetected = CheckForTurnBack(Current_object_list, Previous_object_List)
    if Current_orientation==0 or Previous_orientation==0:
        pass

    if TurnBackDetected == False:
        if Current_orientation =="Mid" and Previous_orientation =="Left":
            Announcement = Current_object_list[Current_object_index] + "is in your right."
        elif Current_orientation =="Mid" and Previous_orientation =="Right":
            Announcement = Current_object_list[Current_object_index] +" is in your left."
        elif Current_orientation =="Left" and Previous_orientation =="Right":
            Announcement = Current_object_list[Current_object_index] +" is in your right."
        elif Current_orientation =="Left" and Previous_orientation =="Mid":
            Announcement = Current_object_list[Current_object_index] +" is in your right."
        elif Current_orientation =="Right" and Previous_orientation =="Left":
            Announcement = Current_object_list[Current_object_index] +" is in your right."
        elif Current_orientation =="Right" and Previous_orientation =="Mid":
            Announcement = Current_object_list[Current_object_index] +" is in your right."
        elif (Current_orientation=="Right" and Previous_orientation=="Right") and (Current_object_index!=Previous_orientation):
            Announcement = Current_object_list[Current_object_index] +" is in your right."
        elif (Current_orientation=="Left" and Previous_orientation=="Left") and (Current_object_index!=Previous_orientation):
            Announcement = Current_object_list[Current_object_index] +" is in your Left."
        else:
            print(TurnBackDetected,Previous_orientation,Current_orientation)
            Announcement = "There is a " + Current_object_list[-1]

            return Announcement

    elif TurnBackDetected == True:
        if Current_orientation=="Left":
            Current_orientation=="Right"
        elif Current_orientation=="right":
            Current_orientation == "left"
        if Previous_orientation=="Right":
            Previous_orientation=="Left"
        elif Previous_orientation=="Left":
            Previous_orientation == "Right"
        if Current_orientation =="Mid" and Previous_orientation =="Left":
            Announcement = Current_object_list[Current_object_index] + "is in your right."
        elif Current_orientation =="Mid" and Previous_orientation =="Right":
            Announcement = Current_object_list[Current_object_index] +" is in your left."
        elif Current_orientation =="Left" and Previous_orientation =="Right":
            Announcement = Current_object_list[Current_object_index] +" is in your right."
        elif Current_orientation =="Left" and Previous_orientation =="Mid":
            Announcement = Current_object_list[Current_object_index] +" is in your right."
        elif Current_orientation =="Right" and Previous_orientation =="Left":
            Announcement = Current_object_list[Current_object_index] +" is in your right."
        elif Current_orientation =="Right" and Previous_orientation =="Mid":
            Announcement = Current_object_list[Current_object_index] +" is in your right."
        elif (Current_orientation=="Right" and Previous_orientation=="Right") and (Current_object_index!=Previous_orientation):
            Announcement = Current_object_list[Current_object_index] +" is in your right."
        elif (Current_orientation=="Left" and Previous_orientation=="Left") and (Current_object_index!=Previous_orientation):
            Announcement = Current_object_list[Current_object_index] +" is in your Left."
        else:
            print(TurnBackDetected,Previous_orientation,Current_orientation)
            Announcement = "There is a " + Current_object_list[-1]

        return Announcement
    return



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
    detect_params = model.predict(source=[frame], conf=0.6, save=False)


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


            # Display class name and confidfence
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
                if type(detected_classes)==list:
                    for i in detected_classes:
                        Current_object_list.append(i)
                        Previous_object_list.append(i)
                else:
                    Current_object_list.append(detected_classes)
                    Previous_object_list.append(detected_classes)

            announcement=navigation_algo_part2(Current_object_list,Previous_object_list)
            print(Previous_object_list)
            print("HIIIIII")
            engine.say(announcement)
            engine.runAndWait()
            Current_object_list=[]

    # Display the resulting frame
    cv2.imshow('ObjectDetection', frame)

    # Terminate run when "Q" pressed
    if cv2.waitKey(1) == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()





