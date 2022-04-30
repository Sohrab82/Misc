import cv2
import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorflow as tf


def exec_conv(image, filter):
    input = np.expand_dims(image, axis=[0, 3])
    kernel = np.expand_dims(filter, axis=[2, 3])
    out = tf.nn.conv2d(input, kernel, strides=[
        1, 1, 1, 1], padding='SAME', data_format='NHWC')

    out = out[0, :, :, 0].numpy()
    out = ((out - np.amin(out)) / np.amax(out) * 255).astype(np.uint8)
    return out.copy()


image = cv2.imread('test.jpg', cv2.IMREAD_GRAYSCALE)
image = image.astype(np.float)
print(image.shape)

# filter formating
filter = np.array([[-3, 0, 1], [-2, 0, 2], [-1, 0, 1]])

filter = np.random.random((7, 7))
filter_smooth = filter.copy()

v_edge = 1 / 5.
v_corner = 1 / 5.
filter_smooth[0, :] = v_edge
filter_smooth[-1, :] = v_edge
filter_smooth[:, 0] = v_edge
filter_smooth[:, -1] = v_edge
filter_smooth[0, 0] = v_corner
filter_smooth[0, -1] = v_corner
filter_smooth[-1, 0] = v_corner
filter_smooth[-1, -1] = v_corner

# convoltion
out = exec_conv(image, filter)
out_smooth = exec_conv(image, filter_smooth)

d_out = out * 1.0 - out_smooth * 1.0
print(d_out)
d_out = np.abs(d_out)

d_out = ((d_out - np.amin(d_out)) / np.amax(d_out) * 255).astype(np.uint8)
d_out = d_out.astype(np.uint8)
cv2.imshow('', np.hstack([out, out_smooth, d_out]))
cv2.waitKey()
