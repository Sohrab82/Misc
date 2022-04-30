# This file compares Element-wise imeplemnted filter with cv2.filter2d & tf.nn.conv2d
import cv2
import numpy as np


def apply_filter(image, filter):
    # element-wise filter
    # applies an filter_n_rowxfilter_n_col filter to the image
    # no padding or stride
    # assuming odd size filter
    (image_n_row, image_n_col) = image.shape
    (filter_n_row, filter_n_col) = filter.shape
    # half size of filter
    filter_n2_row = filter_n_row // 2
    filter_n2_col = filter_n_col // 2
    # output of filter
    image_out = np.zeros(
        (image_n_row - filter_n_row + 1, image_n_col - filter_n_col + 1))
    for r in range(filter_n2_row, image_n_row - filter_n2_row):
        for c in range(filter_n2_col, image_n_col - filter_n2_col):
            # r, c are center point of the filter on the image grid
            image_out[r - filter_n2_row, c - filter_n2_col] = \
                np.sum(np.multiply(filter,
                                   image[r - filter_n2_row:r + filter_n2_row + 1,
                                         c - filter_n2_col:c + filter_n2_col + 1]))
    return image_out


if __name__ == "__main__":
    # define image & filter
    filter = np.array([[-3, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    filter = np.random.random((3, 3))
    filter = np.ones([3, 3])
    image = np.random.random((5, 5))

    print(apply_filter(image, filter))

    # filter2D extrapolates the image at the borders
    # so you can see the output of previous section inside the matrix generated from this function
    # NOTE: it is extra-polation, not zero padding
    print(cv2.filter2D(image, -1, filter))
