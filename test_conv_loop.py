import cv2
import numpy as np
import tensorflow as tf


def exec_conv_el_by_el(image, filter):
    # convolution result
    out_conv = np.zeros_like(image)
    d = int(np.floor(filter.shape[0] / 2))
    for r in range(image.shape[0]):
        for c in range(image.shape[1]):
            tmp = np.zeros_like(filter)
            for fr in range(-d, d + 1):
                for fc in range(-d, d + 1):
                    if (fr + r >= 0) and (fr + r < image.shape[0]) and (fc + c >= 0) and (fc + c < image.shape[1]):
                        tmp[fr + d, fc + d] = image[fr + r, fc + c]
            out_conv[r, c] = np.sum(np.sum(np.multiply(tmp, filter)))

    return out_conv


def exec_conv(image, filter):
    input = np.expand_dims(image, axis=[0, 3])
    kernel = np.expand_dims(filter, axis=[2, 3])
    out = tf.nn.conv2d(input, kernel, strides=[
        1, 1, 1, 1], padding='SAME', data_format='NHWC')

    out = out[0, :, :, 0].numpy()
    out = ((out - np.amin(out)) / np.amax(out) * 255).astype(np.uint8)
    return out.copy()


image = cv2.imread('test_small.png', cv2.IMREAD_GRAYSCALE)
image_f = image.astype(np.float)

# filter formating
filter = np.array([[-3, 0, 1], [-2, 0, 2], [-1, 0, 1]])
print(filter)

# convoltion
out1 = exec_conv(image_f, filter)
out1 = ((out1 - np.amin(out1)) / np.amax(out1) * 255).astype(np.uint8)

# convoltion element-by-element in a loop
out2 = exec_conv_el_by_el(image_f, filter)
out2 = ((out2 - np.amin(out2)) / np.amax(out2) * 255).astype(np.uint8)

print(np.sum(np.sum(out1 - out2)))

cv2.imshow('', np.hstack(
    [image, out1, out2]))
cv2.waitKey()
