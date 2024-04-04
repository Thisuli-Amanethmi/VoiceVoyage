import threading
import numpy as np
import cv2
from ultralytics import YOLO
import random
import pyttsx3
import time

engine = pyttsx3.init()
engine.setProperty('rate', 150)

Previous_object_list = []
Current_object_list = ["first object"]

terminate_thread = False

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()

def thread_function(text):
    global terminate_thread
    while not terminate_thread:
        speak(text)
        time.sleep(1)
    print("Thread terminated gracefully")

def navigation_algorithm(object_list):
    pass

def check_for_turn_back(current_object_list, previous_object_list):
    pass

def navigation_algo_part2(current_object_list, previous_object_list):
    pass

def main():
    class_list = ["bed", "bookshelf", "chair", "clothes-rack", "coffee-table", "commode", "cupboard", "door",
                  "dressing-table", "lamp", "oven", "pantry-cupboards", "refrigerator", "shoe-rack", "sink", "sofa",
                  "staircase", "stove", "table", "tv", "wall-art", "washing-machine", "window"]

    Current_object_list = []

    detection_colors = [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for _ in range(len(class_list))]

    model = YOLO("voiceVoyage_version8_best.pt", "v8")

    frame_wid = 640
    frame_hyt = 480

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Cannot open camera")
        exit()

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
                boxes = detect_params[0].boxes
                box = boxes[i]
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

                if class_list[int(clsID)] not in detected_classes:
                    detected_classes.append(class_list[int(clsID)])

                if detected_classes:
                    if type(detected_classes) == list:
                        for i in detected_classes:
                            Current_object_list.append(i)
                            Previous_object_list.append(i)
                    else:
                        Current_object_list.append(detected_classes)
                        Previous_object_list.append(detected_classes)

                    announcement = navigation_algo_part2(Current_object_list, Previous_object_list)

                    thread = threading.Thread(target=thread_function, args=(announcement,))
                    thread.start()

                    engine.endLoop()

                    print(announcement)

                    Current_object_list = []
        else:
            print("DP = 0")

        cv2.imshow('ObjectDetection', frame)

        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
