import threading

from OntologyGraph import Database as DB, NavAlgo as NV

import numpy as np
import cv2
from ultralytics import YOLO
import random
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150) # words per minute = 150

Previous_object_list = []
Current_object_list = ["first object"]

# Global flag variable to control thread execution
terminate_thread = False


def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # words per minute = 150
    engine.say(text)
    engine.runAndWait()


def thread_function(text):
    global terminate_thread
    while not terminate_thread:
        speak(text)
    print("Thread terminated gracefully")

def navigation_algorithm(object_list):
    direction_counts = {'left': 0, 'right': 0, 'mid': 0}
    object_indices = {'left': None, 'right': None, 'mid': None}
    direction_mapping = {
        'left': ['NV.queryLeft', 'NV.queryFarLeft'],
        'right': ['NV.Right', 'NV.queryFarRight'],
        'mid': ['NV.queryCenter', 'NV.front']
    }

    for obj in object_list:
        for direction, objects in direction_mapping.items():
            if obj in objects:
                direction_counts[direction] += 1
                if object_indices[direction] is None:
                    object_indices[direction] = object_list.index(obj)

    max_direction = max(direction_counts, key=direction_counts.get)
    if direction_counts[max_direction] > 0:
        return max_direction, object_indices[max_direction]
    return None, None

def check_for_turn_back(current_object_list, previous_object_list):
    return len(current_object_list) >= 2 and len(previous_object_list) >= 2 and \
           current_object_list[1] in previous_object_list[-2:]

def navigation_algo_part2(current_object_list, previous_object_list):
    current_orientation, current_object_index = navigation_algorithm(current_object_list)
    previous_orientation, _ = navigation_algorithm(previous_object_list[-1:])
    turn_back_detected = check_for_turn_back(current_object_list, previous_object_list)

    if current_orientation is None or previous_orientation is None:
        return

    if turn_back_detected:
        orientation_switch = {'left': 'right', 'right': 'left'}
        current_orientation = orientation_switch.get(current_orientation, current_orientation)
        previous_orientation = orientation_switch.get(previous_orientation, previous_orientation)

    announcement = "There is a " + current_object_list[current_object_index]
    if current_orientation == "mid":
        side = "right" if previous_orientation == "left" else "left"
        announcement += " is in your " + side + "."
    elif current_orientation != previous_orientation:
        announcement += " is in your right."

    return announcement



def main():
    class_list = ["bed", "bookshelf", "chair", "clothes-rack", "coffee-table", "commode", "cupboard", "door",
                  "dressing-table", "lamp", "oven", "pantry-cupboards", "refrigerator", "shoe-rack", "sink", "sofa",
                  "staircase", "stove", "table", "tv", "wall-art", "washing-machine", "window"]

    Current_object_list = []
    # print(class_list)

    # Generate random colors for class list
    detection_colors = []
    for i in range(len(class_list)):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        detection_colors.append((b, g, r))

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
        # frame = cv2.resize(frame, (frame_wid, frame_hyt))

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
                    if type(detected_classes) == list:
                        for i in detected_classes:
                            Current_object_list.append(i)
                            Previous_object_list.append(i)
                    else:
                        Current_object_list.append(detected_classes)
                        Previous_object_list.append(detected_classes)

                print(Current_object_list)
                print(Previous_object_list)
                announcement = navigation_algo_part2(Current_object_list, Previous_object_list)
                print("HIIIIII")

                # Start a new thread to speak the announcement
                thread = threading.Thread(target=thread_function, args=(announcement,))
                thread.start()
                # To terminate the thread, set the flag variable
                # terminate_thread = False

                engine.endLoop()

                # engine.say(announcement)
                print(announcement)
                # engine.runAndWait()

                Current_object_list = []
        else:
            print("DP = 0")

        # Display the resulting frame
        cv2.imshow('ObjectDetection', frame)

        # Terminate run when "Q" pressed
        if cv2.waitKey(1) == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

