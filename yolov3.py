import tensorflow as tf

# momentum parameter in batch normalization
_BATCH_NORM_DECAY = 0.9

# epsilon parameter in batch normalization
_BATCH_NORM_EPSILON = 1e-05

# alpha parameter for Leaky ReLU activation
_LEAKY_RELU = 0.1

# list of tuples defining anchor box sizes, to predict bounding boxes at different scales. (width, height)
_ANCHORS = [(10, 13), (16, 30), (33, 23),
            (30, 61), (62, 45), (59, 119),
            (116, 90), (156, 198), (373, 326)]


def darknet53(inputs, training, data_format):  # to implement darknet 53 layers - feature extractor
    # return route1, route2, inputs - line 77
    pass


def yolo_convolution_block(inputs, filters, training, data_format):
    # return route, inputs - line 80
    pass


def yolo_layer(inputs, n_classes, anchors, img_size, data_format):
    # return detect1 - line 83
    pass


def conv2d_fixed_padding(route, filters, kernel_size, data_format):
    # return inputs - line 87 & 98
    pass


def batch_norm(inputs, training, data_format):
    # return inputs - line 89 & 99
    pass


def upsample(inputs, out_shape, data_format):
    # return inputs - line 91 & 102
    pass


def build_boxes(inputs):
    # return inputs - line 112
    pass


def non_max_suppression(inputs, n_classes, max_output_size, iou_threshold, confidence_threshold):
    # return boxes_dicts - line 116
    pass


def __call__(self, inputs, training):
# self: an object, inputs: a tensor representing a batch of input images, training: a boolean, whether to use in training or inference mode

    with tf.variable_scope('yolo_v3_model'):  # to create a variable scope named, yolo_v3_model
        if self.data_format == 'channels_first':  # to check whether the data format ia set to channels_first or not
            # In 'channels_first', the channel dimension comes first in the tensor shape, followed by spatial dimensions. It is represented as [batch_size, channels, height, width].
            # In 'channels_last', the spatial dimensions come before the channel dimension. It is represented as [batch_size, height, width, channels].
            # if it's true, then
            inputs = tf.transpose(inputs, [0, 3, 1, 2])  # to change the ordering of its dimensions
            # order:
            # 0th -> 0 = the batch dimension
            # 1st -> 3 = second dimension
            # 2nd -> 1 = 0th dimension
            # 3rd -> 2 = first dimension

        inputs = inputs/255  # to normalizes the input images by dividing all pixel values by 255,
        # and scaling them to the range of [0, 1]

        # to extract features
        route1, route2, inputs = darknet53(inputs, training=training, data_format=self.data_format)

        # to extract high level features
        route, inputs = yolo_convolution_block(inputs, filters=512, training=training, data_format=self.data_format)
        # the results will be pass to yolo_layer
        # yolo_layer - to detect objects using a specific set of anchors and the no. of classes provided
        detect1 = yolo_layer(inputs, n_classes=self.n_classes, anchors=_ANCHORS[6:9], img_size=self.model_size,
                             data_format=self.data_format)

        # detect 2
        inputs = conv2d_fixed_padding(route, filters=256, kernel_size=1, data_format=self.data_format)
        inputs = batch_norm(inputs, training=training, data_format=self.data_format)
        inputs = tf.nn.leaky_relu(inputs, alpha=_LEAKY_RELU)
        upsample_size = route2.get_shape().as_list()
        inputs = upsample(inputs, out_shape=upsample_size, data_format=self.data_format)
        axis = 1 if self.data_format == 'channels_first' else 3
        inputs = tf.concat([inputs, route2], axis=axis)
        route, inputs = yolo_convolution_block(inputs, filters=256, training=training, data_format=self.data_format)
        detect2 = yolo_layer(inputs, n_classes=self.n_classes, anchors=_ANCHORS[3:6], img_size=self.model_size, data_format=self.data_format)

        # detect 3
        inputs = conv2d_fixed_padding(route, filters=128, kernel_size=1, data_format=self.data_format)
        inputs = batch_norm(inputs, training=training, data_format=self.data_format)
        inputs = tf.nn.leaky_relu(inputs, alpha=_LEAKY_RELU)
        upsample_size = route1.get_shape().as_list()
        inputs = upsample(inputs, out_shape=upsample_size, data_format=self.data_format)
        inputs = tf.concat([inputs, route1], axis=axis)
        route, inputs = yolo_convolution_block(inputs, filters=128, training=training, data_format=self.data_format)
        detect3 = yolo_layer(inputs, n_classes=self.n_classes, anchors=_ANCHORS[0:3], img_size=self.model_size, data_format=self.data_format)

        # concatenates all the tensors (results of all detect 1, 2 & 3) along a specified axis
        # axis= 1 means concatenation along the horizontal axis (columns)
        inputs = tf.concat([detect1, detect2, detect3], axis=1)

        # processing the concatenated detections to compute bounding box coordinates, confidence scores, and class probabilities
        inputs = build_boxes(inputs)

        # finally, filtering out overlapping bounding boxes and refine the predictions
        # this returns a list containing dictionaries of class-to-boxes for each sample in the batch
        boxes_dicts = non_max_suppression(inputs, n_classes=self.n_classes, max_output_size=self.max_output_size, iou_threshold=self.iou_threshold, confidence_threshold=self.confidence_threshold)

        return boxes_dicts
