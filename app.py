from flask import Flask, jsonify

app = Flask(__name__)

# Define a flag to indicate whether object detection is running
object_detection_running = False

@app.route('/start_detection', methods=['GET'])
def start_detection():
    global object_detection_running
    
    if not object_detection_running:
        # Start the object detection process (simulate starting the camera and detecting objects)
        object_detection_running = True
        
        # You can perform any initialization or start any background tasks here
        
        return jsonify({'message': 'Object detection started.'}), 200
    else:
        return jsonify({'message': 'Object detection is already running.'}), 200

@app.route('/stop_detection', methods=['GET'])
def stop_detection():
    global object_detection_running
    
    if object_detection_running:
        # Stop the object detection process (simulate stopping the camera and object detection)
        object_detection_running = False
        
        # You can perform any cleanup or stop any background tasks here
        
        return jsonify({'message': 'Object detection stopped.'}), 200
    else:
        return jsonify({'message': 'Object detection is not running.'}), 200

if __name__ == '__main__':
    print("Starting Flask server...")
    app.run(host='0.0.0.0', port=5000)


