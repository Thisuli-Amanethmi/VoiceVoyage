import multiprocessing
import os

from ultralytics import YOLO


def list_subdir(directory):
    subdirectories = []
    for entry in os.listdir(directory):
        if os.path.isdir(os.path.join(directory, entry)):
            subdirectories.append(entry)
    # return subdirectories
    for file_path in subdirectories:
        print(file_path)


def run_yolo(source_index):
    # initializing the yolo model
    model = YOLO('voiceVoyage_version8_best.pt')
    # running inference and saving results
    results = model(source=source_index, show=True, conf=0.6, save=True, save_crop=True, project='runs/detect', name='inference',
                    exist_ok=True)


def main():
    # specifying the directory where the saved results are stored
    directory_path = "runs/detect/inference/crops"
    # setting the source_index
    source_index = 0  # laptop cam
    # source_index = 1 webcam (external cam)

    # process for yolo inference
    yolo_process = multiprocessing.Process(target=run_yolo, args=(source_index,))

    # process for listing subdirectories
    subdir_process = multiprocessing.Process(target=list_subdir, args=(directory_path,))

    # starting both processes
    yolo_process.start()
    subdir_process.start()


if __name__ == "__main__":
    main()


# results1 = model.predict(source='test_images/bathroom.jpg', show=True, conf=0.6, save=True)
# results2 = model.predict(source='test_images/bathroom_2.jpg', show=True, conf=0.6, save=True)
# results3 = model.predict(source='test_images/bathroom_3.jpg', show=True, conf=0.6, save=True)
# results4 = model.predict(source='test_images/bedroom.jpg', show=True, conf=0.6, save=True)
# results5 = model.predict(source='test_images/bedroom_2.jpeg', show=True, conf=0.6, save=True)
# results6 = model.predict(source='test_images/bedroom_3.jpg', show=True, conf=0.6, save=True)
# results7 = model.predict(source='test_images/closet.jpg', show=True, conf=0.6, save=True)
# results8 = model.predict(source='test_images/kitchen.jpg', show=True, conf=0.6, save=True)
# results9 = model.predict(source='test_images/livingroom.jpg', show=True, conf=0.6, save=True)
# results10 = model.predict(source='test_images/livingroom_2.jpg', show=True, conf=0.6, save=True)
# results11 = model.predict(source='test_images/livingroom_3.jpg', show=True, conf=0.6, save=True)
# results12 = model.predict(source='test_images/livingroom_4.jpg', show=True, conf=0.6, save=True)
