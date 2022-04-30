import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('threshold_sample.jpg', 0)

any_number_but_zero = 255
thresh_val = 127

ret, thresh1 = cv2.threshold(
    img, thresh_val, any_number_but_zero, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(
    img, thresh_val, any_number_but_zero, cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(
    img, thresh_val, any_number_but_zero, cv2.THRESH_TRUNC)
ret, thresh4 = cv2.threshold(
    img, thresh_val, any_number_but_zero, cv2.THRESH_TOZERO)
ret, thresh5 = cv2.threshold(
    img, thresh_val, any_number_but_zero, cv2.THRESH_TOZERO_INV)

titles = ['Original Image', 'BINARY',
          'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

for i in range(6):
    plt.subplot(2, 3, i + 1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
