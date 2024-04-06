import time
from OntologyGraph import Database as DB, NavAlgo as NV
import cv2
from ultralytics import YOLO
import random
import pyttsx3
from ObjectDetection import OntologyExtraction as OE


# Initialize the text-to-speech engine

engine = pyttsx3.init()

<<<<<<< Updated upstream

#Get spatial relationship with objects using an ontology
=======
# Lists to keep track of objects
Previous_object_list = []
Current_object_list = []
Spatial_relationship = {}

######################
# Get spatial relationship with objects using an ontology
>>>>>>> Stashed changes
def Get_spatial_relationship_with_objects():
    Spatial_relationship = {"Object1": [], "relationship": [], "Object2": []}
    relationships = ["oppositeOf", "adjacentTo", "near"]

    for j in relationships:
        objects, relation = OE.Spatial_relationships(j)
        for i in range(len(objects) // 2):
            Spatial_relationship["Object1"].append(objects[2 * i])
            Spatial_relationship["Object2"].append(objects[2 * i + 1])
            Spatial_relationship["relationship"].append(relation)
    return Spatial_relationship
############

<<<<<<< Updated upstream

def Check_the_spacial_relationship_of_current_objects(Spatial_relationship,Current_objects):
    # Initialize a list to hold announcements
=======
def Check_the_spatial_relationship_of_current_objects(Spatial_relationship, Current_objects):
>>>>>>> Stashed changes
    announcements = []

    for current_object in Current_objects:
        if current_object in Spatial_relationship["Object1"]:
            Index = Spatial_relationship["Object1"].index(current_object)
            relation = Spatial_relationship["relationship"][Index]
            obj2 = Spatial_relationship["Object2"][Index]
<<<<<<< Updated upstream
            announcement_for_spatial_relation = "The " + current_object + " is " + relation + " " + obj2
            announcements = announcements.append(announcement_for_spatial_relation)
        # Check if the current object is in the Object2 list
=======
            announcements.append(f"The {current_object} is {relation} {obj2}")
>>>>>>> Stashed changes
        elif current_object in Spatial_relationship["Object2"]:
            Index = Spatial_relationship["Object2"].index(current_object)
            relation = Spatial_relationship["relationship"][Index]
            obj1 = Spatial_relationship["Object1"][Index]
<<<<<<< Updated upstream
            announcement_for_spatial_relation = "The " + current_object + " is " + relation + " to " + obj1
            announcements = announcements.append(announcement_for_spatial_relation)
=======
            announcements.append(f"The {current_object} is {relation} to {obj1}")
>>>>>>> Stashed changes

    return ", ".join(announcements) if announcements else " "

<<<<<<< Updated upstream

=======
###################
>>>>>>> Stashed changes
def navigation_algorithm(object_list):
    direction_counts = {'left': 0, 'right': 0, 'mid': 0}
    object_indices = {'left': [], 'right': [], 'mid': []}
    direction_mapping = {
        'left': [NV.queryLeft, NV.queryFarLeft],
        'right': [NV.Right, NV.queryFarRight],
        'mid': [NV.queryCenter, NV.front]
    }

    for obj in object_list:
        for direction, objects in direction_mapping.items():
            if obj in objects:
                direction_counts[direction] += 1
                object_indices[direction].append(object_list.index(obj))

    max_direction = max(direction_counts, key=direction_counts.get)
    return max_direction, object_indices[max_direction][0] if direction_counts[max_direction] > 0 else 0



def check_for_turn_back(current_object_list, previous_object_list):
    return set(current_object_list[-2:]).intersection(set(previous_object_list[-2:]))

<<<<<<< Updated upstream

=======
################################################
>>>>>>> Stashed changes
def navigation_algo_part2(current_object_list, previous_object_list):
    if not current_object_list or not previous_object_list:
        return "None part 2"

    current_orientation, current_object_index = navigation_algorithm(current_object_list)
    previous_orientation, _ = navigation_algorithm(previous_object_list[-2:])

    if check_for_turn_back(current_object_list, previous_object_list):
        orientation_switch = {'left': 'right', 'right': 'left', 'mid': 'mid'}
        current_orientation = orientation_switch.get(current_orientation, current_orientation)
<<<<<<< Updated upstream
        previous_orientation = orientation_switch.get(previous_orientation, previous_orientation)
    announcement = " "

    if current_orientation == "mid":
        side = "right" if previous_orientation == "left" else "left"
        announcement = " is in your " + side + "."
    elif current_orientation != previous_orientation:
        announcement = " is in your right."
=======

    announcement = f"There is a {current_object_list[current_object_index]} in your {current_orientation}." if current_object_index is not None else ""
>>>>>>> Stashed changes

    return announcement


<<<<<<< Updated upstream
=======

>>>>>>> Stashed changes
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

<<<<<<< Updated upstream
    # perform some slow operation
    time.sleep(2)

    cv2.imshow('frame', frame)
=======
    # peform some slow operation
    #time.sleep(2)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
>>>>>>> Stashed changes

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
            Spatial_relation_dict=Get_spatial_relationship_with_objects()
            print(Spatial_relation_dict)
            Spatial_announcement= Check_the_spatial_relationship_of_current_objects(Spatial_relation_dict,Current_object_list)
            announcement=navigation_algo_part2(Current_object_list,Previous_object_list)
            if Spatial_announcement!=" ":
                engine.say(Spatial_announcement+announcement)
            else:
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

