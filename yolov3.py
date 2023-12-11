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


def darknet53_residual_block(inputs, filters, training, data_format, strides=1):
    # creates a residual block for Darknet

    shortcut = inputs

    inputs = conv2d_fixed_padding(inputs, filters=filters, kernel_size=1, strides=strides, data_format=data_format)
    inputs = batch_norm(inputs, training=training, data_format=data_format)
    inputs = tf.nn.leaky_relu(inputs, alpha=_LEAKY_RELU)

    inputs = conv2d_fixed_padding(inputs, filters=2 * filters, kernel_size=3, strides=strides, data_format=data_format)
    inputs = batch_norm(inputs, training=training, data_format=data_format)
    inputs = tf.nn.leaky_relu(inputs, alpha=_LEAKY_RELU)

    inputs += shortcut

    return inputs


def darknet53(inputs, training, data_format):  # to implement darknet 53 layers - feature extractor
    # return route1, route2, inputs - line 77

    # INITIAL CONVOLUTIONAL BLOCKS
    # performs a convolution operation with fixed padding to maintain spatial dimensions
    inputs = conv2d_fixed_padding(inputs, filters=32, kernel_size=3, data_format=data_format)
    # applies batch normalization to the convolutional output
    inputs = batch_norm(inputs, training=training, data_format=data_format)
    # applies Leaky ReLU activation function to introduce non-linearity
    # Leaky ReLU prevents neuron inactivity by allowing a small gradient for negative inputs, enhancing deep network learning and performance compared to ReLU
    inputs = tf.nn.leaky_relu(inputs, alpha=_LEAKY_RELU)

    # DOWNSAMPLING
    # Performing another convolutional operation with larger filters and a stride of 2 to downsample the feature maps
    inputs = conv2d_fixed_padding(inputs, filters=64, kernel_size=3, strides=2, data_format=data_format)
    inputs = batch_norm(inputs, training=training, data_format=data_format)
    inputs = tf.nn.leaky_relu(inputs, alpha=_LEAKY_RELU)

    # RESIDUAL BLOCKS & FEATURE EXTRACTION
    # to create a residual block
    # this block contains convolutional layers, batch normalization, and activation functions to further extract features.
    inputs = darknet53_residual_block(inputs, filters=32, training=training, data_format=data_format)

    # Successive Feature Extraction at Different Scales
    # repeat the process of applying convolutional blocks, downsampling, and residual blocks, each aimed at capturing features at varying scales
    inputs = conv2d_fixed_padding(inputs, filters=128, kernel_size=3, strides=2, data_format=data_format)
    inputs = batch_norm(inputs, training=training, data_format=data_format)
    inputs = tf.nn.leaky_relu(inputs, alpha=_LEAKY_RELU)

    for _ in range(2):
        inputs = darknet53_residual_block(inputs, filters=64, training=training, data_format=data_format)

    inputs = conv2d_fixed_padding(inputs, filters=256, kernel_size=3, strides=2, data_format=data_format)
    inputs = batch_norm(inputs, training=training, data_format=data_format)
    inputs = tf.nn.leaky_relu(inputs, alpha=_LEAKY_RELU)

    for _ in range(8):
        inputs = darknet53_residual_block(inputs, filters=128, training=training, data_format=data_format)

    route1 = inputs

    inputs = conv2d_fixed_padding(inputs, filters=512, kernel_size=3, strides=2, data_format=data_format)
    inputs = batch_norm(inputs, training=training, data_format=data_format)
    inputs = tf.nn.leaky_relu(inputs, alpha=_LEAKY_RELU)

    for _ in range(8):
        inputs = darknet53_residual_block(inputs, filters=256, training=training, data_format=data_format)

    route2 = inputs

    inputs = conv2d_fixed_padding(inputs, filters=1024, kernel_size=3, strides=2, data_format=data_format)
    inputs = batch_norm(inputs, training=training, data_format=data_format)
    inputs = tf.nn.leaky_relu(inputs, alpha=_LEAKY_RELU)

    for _ in range(4):
        inputs = darknet53_residual_block(inputs, filters=512, training=training, data_format=data_format)

    return route1, route2, inputs


def yolo_convolution_block(inputs, filters, training, data_format):
    # return route, inputs - line 80
    # creates convolution operations layer used after Darknet

    inputs = conv2d_fixed_padding(inputs, filters=filters, kernel_size=1, data_format=data_format)
    inputs = batch_norm(inputs, training=training, data_format=data_format)
    inputs = tf.nn.leaky_relu(inputs, alpha=_LEAKY_RELU)

    inputs = conv2d_fixed_padding(inputs, filters=2 * filters, kernel_size=3, data_format=data_format)
    inputs = batch_norm(inputs, training=training, data_format=data_format)
    inputs = tf.nn.leaky_relu(inputs, alpha=_LEAKY_RELU)

    inputs = conv2d_fixed_padding(inputs, filters=filters, kernel_size=1, data_format=data_format)
    inputs = batch_norm(inputs, training=training, data_format=data_format)
    inputs = tf.nn.leaky_relu(inputs, alpha=_LEAKY_RELU)

    inputs = conv2d_fixed_padding(inputs, filters=2 * filters, kernel_size=3, data_format=data_format)
    inputs = batch_norm(inputs, training=training, data_format=data_format)
    inputs = tf.nn.leaky_relu(inputs, alpha=_LEAKY_RELU)

    inputs = conv2d_fixed_padding(inputs, filters=filters, kernel_size=1, data_format=data_format)
    inputs = batch_norm(inputs, training=training, data_format=data_format)
    inputs = tf.nn.leaky_relu(inputs, alpha=_LEAKY_RELU)

    route = inputs

    inputs = conv2d_fixed_padding(inputs, filters=2 * filters, kernel_size=3, data_format=data_format)
    inputs = batch_norm(inputs, training=training, data_format=data_format)
    inputs = tf.nn.leaky_relu(inputs, alpha=_LEAKY_RELU)

    return route, inputs


def yolo_layer(inputs, n_classes, anchors, img_size, data_format):
    # return detect1 - line 83

    """Creates Yolo final detection layer.

        Detects boxes with respect to anchors.

        Args:
            inputs: Tensor input.
            n_classes: Number of labels.
            anchors: A list of anchor sizes.
            img_size: The input size of the model.
            data_format: The input format.

        Returns:
            Tensor output.
        """
    n_anchors = len(anchors)

    inputs = tf.keras.layers.Conv2D(inputs, filters=n_anchors * (5 + n_classes), kernel_size=1, strides=1, use_bias=True, data_format=data_format)

    shape = inputs.get_shape().as_list()
    grid_shape = shape[2:4] if data_format == 'channels_first' else shape[1:3]
    if data_format == 'channels_first':
        inputs = tf.transpose(inputs, [0, 2, 3, 1])
    inputs = tf.reshape(inputs, [-1, n_anchors * grid_shape[0] * grid_shape[1],
                                 5 + n_classes])

    strides = (img_size[0] // grid_shape[0], img_size[1] // grid_shape[1])

    box_centers, box_shapes, confidence, classes = \
        tf.split(inputs, [2, 2, 1, n_classes], axis=-1)

    x = tf.range(grid_shape[0], dtype=tf.float32)
    y = tf.range(grid_shape[1], dtype=tf.float32)
    x_offset, y_offset = tf.meshgrid(x, y)
    x_offset = tf.reshape(x_offset, (-1, 1))
    y_offset = tf.reshape(y_offset, (-1, 1))
    x_y_offset = tf.concat([x_offset, y_offset], axis=-1)
    x_y_offset = tf.tile(x_y_offset, [1, n_anchors])
    x_y_offset = tf.reshape(x_y_offset, [1, -1, 2])
    box_centers = tf.nn.sigmoid(box_centers)
    box_centers = (box_centers + x_y_offset) * strides

    anchors = tf.tile(anchors, [grid_shape[0] * grid_shape[1], 1])
    box_shapes = tf.exp(box_shapes) * tf.to_float(anchors)

    confidence = tf.nn.sigmoid(confidence)

    classes = tf.nn.sigmoid(classes)

    inputs = tf.concat([box_centers, box_shapes,
                        confidence, classes], axis=-1)

    return inputs


def fixed_padding(inputs, kernel_size, data_format):
    """ResNet implementation of fixed padding.

    Pads the input along the spatial dimensions independently of input size.

    Args:
        inputs: Tensor input to be padded.
        kernel_size: The kernel to be used in the conv2d or max_pool2d.
        data_format: The input format.
    Returns:
        A tensor with the same format as the input.
    """
    pad_total = kernel_size - 1
    pad_beg = pad_total // 2
    pad_end = pad_total - pad_beg

    if data_format == 'channels_first':
        padded_inputs = tf.pad(inputs, [[0, 0], [0, 0],
                                        [pad_beg, pad_end],
                                        [pad_beg, pad_end]])
    else:
        padded_inputs = tf.pad(inputs, [[0, 0], [pad_beg, pad_end],
                                        [pad_beg, pad_end], [0, 0]])
    return padded_inputs


def conv2d_fixed_padding(inputs, filters, kernel_size, data_format, strides=1):
    # return inputs - line 87 & 98

    # strided 2-D convolution with explicit padding
    if strides > 1:
        inputs = fixed_padding(inputs, kernel_size, data_format)

    return tf.keras.layers.Conv2D(
        filters=filters, kernel_size=kernel_size,
        strides=strides, padding=('SAME' if strides == 1 else 'VALID'),
        use_bias=False, data_format=data_format)(inputs)


def batch_norm(inputs, training, data_format):
    # return inputs - line 89 & 99
    # performs a batch normalization using a standard set of parameters."""
    return tf.keras.layers.BatchNormalization(axis=1 if data_format == 'channels_first' else 3, momentum=_BATCH_NORM_DECAY, epsilon=_BATCH_NORM_EPSILON, scale=True, training=training)(inputs)


def upsample(inputs, out_shape, data_format):
    # return inputs - line 91 & 102

    # upsamples to `out_shape` using nearest neighbor interpolation
    if data_format == 'channels_first':
        inputs = tf.transpose(inputs, [0, 2, 3, 1])
        new_height = out_shape[3]
        new_width = out_shape[2]
    else:
        new_height = out_shape[2]
        new_width = out_shape[1]

    inputs = tf.image.resize_nearest_neighbor(inputs, (new_height, new_width))

    if data_format == 'channels_first':
        inputs = tf.transpose(inputs, [0, 3, 1, 2])

    return inputs


def build_boxes(inputs):
    # return inputs - line 112

    # computes top left and bottom right points of the boxes
    center_x, center_y, width, height, confidence, classes = \
        tf.split(inputs, [1, 1, 1, 1, 1, -1], axis=-1)

    top_left_x = center_x - width / 2
    top_left_y = center_y - height / 2
    bottom_right_x = center_x + width / 2
    bottom_right_y = center_y + height / 2

    boxes = tf.concat([top_left_x, top_left_y,
                       bottom_right_x, bottom_right_y,
                       confidence, classes], axis=-1)

    return boxes


def non_max_suppression(inputs, n_classes, max_output_size, iou_threshold, confidence_threshold):
    # return boxes_dicts - line 116

    # performs non-max suppression separately for each class
    # will return a list containing class-to-boxes dictionaries for each sample in the batch.

    batch = tf.unstack(inputs)
    boxes_dicts = []
    for boxes in batch:
        boxes = tf.boolean_mask(boxes, boxes[:, 4] > confidence_threshold)
        classes = tf.argmax(boxes[:, 5:], axis=-1)
        classes = tf.expand_dims(tf.to_float(classes), axis=-1)
        boxes = tf.concat([boxes[:, :5], classes], axis=-1)

        boxes_dict = dict()
        for cls in range(n_classes):
            mask = tf.equal(boxes[:, 5], cls)
            mask_shape = mask.get_shape()
            if mask_shape.ndims != 0:
                class_boxes = tf.boolean_mask(boxes, mask)
                boxes_coords, boxes_conf_scores, _ = tf.split(class_boxes,
                                                              [4, 1, -1],
                                                              axis=-1)
                boxes_conf_scores = tf.reshape(boxes_conf_scores, [-1])
                indices = tf.image.non_max_suppression(boxes_coords,
                                                       boxes_conf_scores,
                                                       max_output_size,
                                                       iou_threshold)
                class_boxes = tf.gather(class_boxes, indices)
                boxes_dict[cls] = class_boxes[:, :5]

        boxes_dicts.append(boxes_dict)

    return boxes_dicts


class Yolo_v3:
    # yolo v3 model class

    def __init__(self, n_classes, model_size, max_output_size, iou_threshold,
                 confidence_threshold, data_format=None):

        # n_classes: number of class labels
        # model_size: input size of the model
        # max_output_size: max number of boxes to be selected for each class
        # iou_threshold: threshold for the IOU
        # confidence_threshold: threshold for the confidence score
        # data_format: input format.

        if not data_format:
            if tf.test.is_built_with_cuda():
                data_format = 'channels_first'
            else:
                data_format = 'channels_last'
        # In 'channels_first', the channel dimension comes first in the tensor shape, followed by spatial dimensions. It is represented as [batch_size, channels, height, width].
        # In 'channels_last', the spatial dimensions come before the channel dimension. It is represented as [batch_size, height, width, channels].

        self.n_classes = n_classes
        self.model_size = model_size
        self.max_output_size = max_output_size
        self.iou_threshold = iou_threshold
        self.confidence_threshold = confidence_threshold
        self.data_format = data_format

    def __call__(self, inputs, training):
        # self: an object, inputs: a tensor representing a batch of input images, training: a boolean, whether to use in training or inference mode

        with tf.compat.v1.variable_scope('yolo_v3_model'):  # to create a variable scope named, yolo_v3_model
            if self.data_format == 'channels_first':  # to check whether the data format ia set to channels_first or not
                # if it's true, then
                inputs = tf.transpose(inputs, [0, 3, 1, 2])  # to change the ordering of its dimensions
                # order:
                # 0th -> 0 = the batch dimension
                # 1st -> 3 = second dimension
                # 2nd -> 1 = 0th dimension
                # 3rd -> 2 = first dimension

            inputs = inputs / 255  # to normalizes the input images by dividing all pixel values by 255,
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
            detect2 = yolo_layer(inputs, n_classes=self.n_classes, anchors=_ANCHORS[3:6], img_size=self.model_size,
                                 data_format=self.data_format)

            # detect 3
            inputs = conv2d_fixed_padding(route, filters=128, kernel_size=1, data_format=self.data_format)
            inputs = batch_norm(inputs, training=training, data_format=self.data_format)
            inputs = tf.nn.leaky_relu(inputs, alpha=_LEAKY_RELU)
            upsample_size = route1.get_shape().as_list()
            inputs = upsample(inputs, out_shape=upsample_size, data_format=self.data_format)
            inputs = tf.concat([inputs, route1], axis=axis)
            route, inputs = yolo_convolution_block(inputs, filters=128, training=training, data_format=self.data_format)
            detect3 = yolo_layer(inputs, n_classes=self.n_classes, anchors=_ANCHORS[0:3], img_size=self.model_size,
                                 data_format=self.data_format)

            # concatenates all the tensors (results of all detect 1, 2 & 3) along a specified axis
            # axis= 1 means concatenation along the horizontal axis (columns)
            inputs = tf.concat([detect1, detect2, detect3], axis=1)

            # processing the concatenated detections to compute bounding box coordinates, confidence scores, and class probabilities
            inputs = build_boxes(inputs)

            # finally, filtering out overlapping bounding boxes and refine the predictions
            # this returns a list containing dictionaries of class-to-boxes for each sample in the batch
            boxes_dicts = non_max_suppression(inputs, n_classes=self.n_classes, max_output_size=self.max_output_size,
                                              iou_threshold=self.iou_threshold,
                                              confidence_threshold=self.confidence_threshold)

            return boxes_dicts

