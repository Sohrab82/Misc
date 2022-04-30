# Import the necessary packages
import numpy as np
import cv2


def translate(image, x, y):
    # Define the translation matrix and perform the translation
    M = np.float32([[1, 0, x], [0, 1, y]])
    shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
    # Return the translated image
    return shifted


def rotate(image, angle, center=None, scale=1.0):
    # Grab the dimensions of the image
    (h, w) = image.shape[:2]
    # If the center is None, initialize it as the center of
    # the image
    if center is None:
        center = (w / 2, h / 2)

    # Perform the rotation
    M = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(image, M, (w, h))
    # Return the rotated image
    return rotated


def resize(image, width=None, height=None, inter=cv2.INTER_AREA):
    # initialize the dimensions of the image to be resized and
    # grab the image size
    dim = None
    (h, w) = image.shape[:2]

    # if both the width and height are None, then return the
    # original image
    if width is None and height is None:
        return image

    # check to see if the width is None
    if width is None:
        # calculate the ratio of the height and construct the
        # dimensions
        r = height / float(h)
        dim = (int(w * r), height)

    # otherwise, the height is None
    else:
        # calculate the ratio of the width and construct the
        # dimensions
        r = width / float(w)
        dim = (width, int(h * r))

    # resize the image
    resized = cv2.resize(image, dim, interpolation=inter)

    # return the resized image
    return resized

# plot multiple images


def imshow_multiple(*args):
    margin_len = 30
    margin = np.ones((margin_len, args[0].shape[1], 3), dtype='uint8') * 255
    img = np.ones((1, args[0].shape[1], 3), dtype='uint8')

    for arg in args:
        if len(arg.shape) == 2:  # black & white image
            img_tmp = cv2.cvtColor(arg, cv2.COLOR_GRAY2BGR)
        else:
            img_tmp = arg.copy()
        img = np.vstack((img, img_tmp))
        img = np.vstack((img, margin))

    width = 600
    (h, w) = img.shape[:2]
    r = width / float(w)
    dim = (width, int(h * r))

    # resize the image
    resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    # print(resized.shape)
    # print(img[40][1:10])
    cv2.imshow("window", resized)
