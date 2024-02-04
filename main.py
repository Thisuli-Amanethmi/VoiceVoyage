#import pandas as pd

#import numpy as np
#import os
import six.moves.urllib as urllib
import sys
import tarfile
#import tensorflow as tf
import zipfile
import pathlib
from collections import defaultdict
from io import StringIO
#from matplotlib import pyplot as plt
#from PIL import Image
#from IPython.display import display

#from object_detection.utils import ops as utils_ops
#from object_detection.utils import label_map_util
#from object_detection.utils import visualization_utils as vis_util

# Metadata DataFrames
# 13 objects
metadata1 = ({
    'ID': [1,2,3,4,5,6,7,8,9,10,11,12,13],
    'Label': ['Wall','Chair','Table','Sofa','TV','Door','Window','Bed','Cupboard','DressingTable','Commode','Sink','Fridge'],
    'File_Path':['']
})
# Staircase
metadata2 = ({
    'ID': [14],
    'Label': ['Staircase'],
    'File_Path':['']
})
# Washing Machine
metadata3 = ({
    'ID': [15],
    'Label': ['WashingMachine'],
    'File_Path':['']
})
# Stove cooker
metadata4 = ({
    'ID': [16],
    'Label': ['Cooker'],
    'File_Path':['']
})
# Dustbin
metadata5 = ({
    'ID': [17],
    'Label': ['Dustbin'],
    'File_Path':['']
})
# Broom
metadata6 = ({
    'ID': [18],
    'Label': ['Broom'],
    'File_Path':['']
})

# Accessing metadata for the first image
#first_image_metadata1 = metadata1[0]
#first_image_metadata2 = metadata2[0]
#first_image_metadata3 = metadata3[0]
#first_image_metadata4 = metadata4[0]
#first_image_metadata5 = metadata5[0]
#first_image_metadata6 = metadata6[0]

#print(first_image_metadata1)


# Staircase
#metadata2 = pd.DataFrame({
    #'ID': [14],
    #'Label': ['Staircase'],
    #'File_Path':['']
#})
# Merge metadata based on the 'ID' column
#combined_metadata = pd.merge(metadata1, metadata2, metadata3, metadata4, metadata5, metadata6, on='ID', how='outer')





#detect the objects and identify the object class in the dataset
# Download and extract the model
def download_model(model_name):
    base_url = 'http://download.tensorflow.org/models/object_detection/'
    model_file = model_name + '.tar.gz'
    #model_dir = tf.keras.utils.get_file(
        #fname=model_name,
        #origin=base_url + model_file,
        #untar=True)
    #return str(model_dir)

MODEL_NAME = 'ssd_inception_v2_coco_2017_11_17'
PATH_TO_MODEL_DIR = download_model(MODEL_NAME)

# Load the model
#PATH_TO_SAVED_MODEL = PATH_TO_MODEL_DIR + "/saved_model"
#model = tf.saved_model.load(str(PATH_TO_SAVED_MODEL))

# Load label map
#PATH_TO_LABELS = os.path.join(PATH_TO_MODEL_DIR, "mscoco_label_map.pbtxt")
#category_index = label_map_util.create_category_index_from_labelmap(PATH_TO_LABELS, use_display_name=True)

# Load image
PATH_TO_IMAGE = 'path/to/your/image.jpg'
#img = Image.open(PATH_TO_IMAGE)
#image_np = np.array(img)

# The input needs to be a tensor, convert it using `tf.convert_to_tensor`.
#input_tensor = tf.convert_to_tensor(image_np)
# The model expects a batch of images, so add an axis with `tf.newaxis`.
#input_tensor = input_tensor[tf.newaxis,...]

# Run inference
#model_fn = model.signatures['serving_default']
#output_dict = model_fn(input_tensor)

# All outputs are batches tensors.
# Convert to numpy arrays, and take index [0] to remove the batch dimension.
# We're only interested in the first num_detections.
#num_detections = int(output_dict.pop('num_detections'))
#output_dict = {key:value[0, :num_detections].numpy()
               #for key,value in output_dict.items()}
#output_dict['num_detections'] = num_detections

# detection_classes should be ints.
#output_dict['detection_classes'] = output_dict['detection_classes'].astype(np.int64)

# Visualization of the results of a detection.
#vis_util.visualize_boxes_and_labels_on_image_array(
            #image_np,
            #output_dict['detection_boxes'],
            #output_dict['detection_classes'],
            #output_dict['detection_scores'],
            #category_index,
            #instance_masks=output_dict.get('detection_masks_reframed', None),
            #use_normalized_coordinates=True,
            #line_thickness=8)

# Display the result
#display(Image.fromarray(image_np))
