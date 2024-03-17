# from flask import Flask, jsonify
#
# app = Flask(__name__)
#
# # Define a flag to indicate whether object detection is running
# object_detection_running = False
#
# @app.route('/start_detection', methods=['GET'])
# def start_detection():
#     global object_detection_running
#
#     if not object_detection_running:
#         # Start the object detection process (simulate starting the camera and detecting objects)
#         object_detection_running = True
#
#         # You can perform any initialization or start any background tasks here
#
#         return jsonify({'message': 'Object detection started.'}), 200
#     else:
#         return jsonify({'message': 'Object detection is already running.'}), 200
#
# @app.route('/stop_detection', methods=['GET'])
# def stop_detection():
#     global object_detection_running
#
#     if object_detection_running:
#         # Stop the object detection process (simulate stopping the camera and object detection)
#         object_detection_running = False
#
#         # You can perform any cleanup or stop any background tasks here
#
#         return jsonify({'message': 'Object detection stopped.'}), 200
#     else:
#         return jsonify({'message': 'Object detection is not running.'}), 200


from flask import Flask, request, jsonify
import multiprocessing
import os
from ultralytics import YOLO

app = Flask(__name__)

model = None  # Initialize model globally for efficiency


def run_yolo(source_index):
    global model
    if model is None:
        model = YOLO('voiceVoyage_version8_best.pt')  # Load model only once
    results = model(source=source_index, show=False, conf=0.6, save=True,
                       save_crop=True, project='runs/detect', name='inference', exist_ok=True)
    return results.pandas().xyxy[0].to_json(orient='records')  # Return JSON for response


@app.route('/detect_objects')
def detect_objects():
    source_index = request.args.get('source_index', 0)  # Get source_index from query parameter
    yolo_process = multiprocessing.Process(target=run_yolo, args=(int(source_index),))
    yolo_process.start()
    yolo_process.join()  # Wait for detection to complete
    results = yolo_process.exitcode  # Retrieve results from process
    return jsonify(results)  # Return results as JSON response


if __name__ == '__main__':
    print("Starting Flask server...")
    app.run(host='0.0.0.0', port=5000)  # Run Flask server on port 5000 (or any preferred port)



