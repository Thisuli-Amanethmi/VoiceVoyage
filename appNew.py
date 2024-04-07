from flask import Flask, render_template, Response, request, jsonify
from ultralytics import YOLO
import pyttsx3

from ObjectDetection import yolo8_custom_live_NEW
from OntologyGraph import RoomFormatNEW
from OntologyGraph import SaveToDBNEW

# Initialize Flask app and text-to-speech engine
app = Flask(__name__)
engine = pyttsx3.init()

# Load YOLOv8 model
model = YOLO("voiceVoyage_version8_best.pt", "v8")

# Global variables for object tracking
Previous_object_list = []
Current_object_list = []

# Flag for stopping object detection
stop_detection_flag = False


@app.route("/")
def index():
    return render_template("index.html")  # Assuming a basic HTML template


def object_detection():
    yolo8_custom_live_NEW.main()


@app.route("/start_detection")
def start_detection():
    return Response(object_detection(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route("/stop_detection")
def stop_detection():
    global cap  # Access the global variable
    cap.release()
    return "Detection Stopped"


# def process_room_format(in_front, to_the_left, far_left, to_the_right, far_right, behind_you, center,
#                         window_near_door, window_on_left_wall, window_on_right_wall, window_on_front_wall):
#     print("hii 1")
#     RoomFormatNEW.room_format_print(in_front, to_the_left, far_left, to_the_right, far_right, behind_you, center,
#                                     window_near_door, window_on_left_wall, window_on_right_wall, window_on_front_wall)
#     print("hii 2")
#     RoomFormatNEW.room_format_rdf(in_front, to_the_left, far_left, to_the_right, far_right, behind_you, center,
#                                   window_near_door, window_on_left_wall, window_on_right_wall, window_on_front_wall)
#
#     # Return a result indicating success or failure
#     return 'Room format processed successfully'
#
#
# @app.route("/room_format")
# def room_format():
#     # Extract parameters sent by the Android application from the request
#     in_front = request.args.get('in_front')
#     to_the_left = request.args.get('to_the_left')
#     far_left = request.args.get('far_left')
#     to_the_right = request.args.get('to_the_right')
#     far_right = request.args.get('far_right')
#     behind_you = request.args.get('behind_you')
#     center = request.args.get('center')
#     window_near_door = request.args.get('window_near_door')
#     window_on_left_wall = request.args.get('window_on_left_wall')
#     window_on_right_wall = request.args.get('window_on_right_wall')
#     window_on_front_wall = request.args.get('window_on_front_wall')
#
#     # result = process_room_format(in_front, to_the_left, far_left, to_the_right, far_right, behind_you, center,
#     #                              window_near_door, window_on_left_wall, window_on_right_wall, window_on_front_wall)
#     #
#     # # Return a response
#     # return jsonify({'result': result})
#
#     return Response(process_room_format(in_front, to_the_left, far_left, to_the_right, far_right, behind_you, center,
#                                  window_near_door, window_on_left_wall, window_on_right_wall, window_on_front_wall))


def inputs_to_save_DB(in_front, to_the_left, far_left, to_the_right, far_right, behind_you, center,
                        window_near_door, window_on_left_wall, window_on_right_wall, window_on_front_wall):
    print("hii 1")
    SaveToDBNEW.save_to_ontology_database(in_front, to_the_left, far_left, to_the_right, far_right, behind_you, center,
                                    window_near_door, window_on_left_wall, window_on_right_wall, window_on_front_wall)
    print("hii 2")

    return 'Room format processed successfully'


@app.route("/save_to_db")
def save_to_db():
    # Extract parameters sent by the Android application from the request
    in_front = request.args.get('in_front')
    to_the_left = request.args.get('to_the_left')
    far_left = request.args.get('far_left')
    to_the_right = request.args.get('to_the_right')
    far_right = request.args.get('far_right')
    behind_you = request.args.get('behind_you')
    center = request.args.get('center')
    window_near_door = request.args.get('window_near_door')
    window_on_left_wall = request.args.get('window_on_left_wall')
    window_on_right_wall = request.args.get('window_on_right_wall')
    window_on_front_wall = request.args.get('window_on_front_wall')

    return Response(inputs_to_save_DB(in_front, to_the_left, far_left, to_the_right, far_right, behind_you, center,
                                 window_near_door, window_on_left_wall, window_on_right_wall, window_on_front_wall))


if __name__ == "__main__":
    app.run(debug=True)


