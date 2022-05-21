import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('threshold_sample.jpg', 0)
 
any_number_but_zero = 255 # this value does not matter
thresh_val = 30

# set anything below the thresold to zero and above it to 255
ret, thresh1 = cv2.threshold(
    img, thresh_val, any_number_but_zero, cv2.THRESH_BINARY)
# set anything below the thresold to 255 and above it to 0
ret, thresh2 = cv2.threshold(
    img, thresh_val, any_number_but_zero, cv2.THRESH_BINARY_INV)
# set anything above the thresold to 255
ret, thresh3 = cv2.threshold(
    img, thresh_val, any_number_but_zero, cv2.THRESH_TRUNC)
# set anything below the thresold to Zero
ret, thresh4 = cv2.threshold(
    img, thresh_val, any_number_but_zero, cv2.THRESH_TOZERO)
# set anything above the thresold to Zero
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
