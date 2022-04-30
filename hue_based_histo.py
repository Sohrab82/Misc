#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 17:30:20 2019

@author: sohrab
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt
import os

path = '/media/sohrab/ntfs/Work/repos/python/my_tf/test_tomorrow/'
fname = "test.jpg"
image = cv2.imread(path + fname)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
num_bins = 255
if not os.path.exists(path + os.path.splitext(fname)[0]):
    os.mkdir(path + os.path.splitext(fname)[0])
path = path + os.path.splitext(fname)[0] + '/'

dh = 37
for hue_range in range(0, 180, dh):
    # for hue_range in [27]:
    lower_range = np.array([hue_range, 0, 0])
    upper_range = np.array([hue_range + dh, 255, 255])

    mask = np.zeros(hsv[0].shape)
    mask = cv2.inRange(hsv, lower_range, upper_range)

    hist = cv2.calcHist([hsv], [1], mask, [num_bins], [0, 255])
    flat_list = [item for sublist in hist.tolist() for item in sublist]
    plt.figure()
    plt.bar(range(0, num_bins), flat_list)
    #plt.ylim([0, 10000])
    plt.title(str(hue_range) + ', saturation')
    plt.plot(hist)
    plt.savefig(path + 'image_' + str(hue_range) + '_sat.png',)

    hist = cv2.calcHist([hsv], [2], mask, [num_bins], [0, 255])
    flat_list = [item for sublist in hist.tolist() for item in sublist]
    plt.figure()
    plt.bar(range(0, num_bins), flat_list)
    plt.title(str(hue_range) + ', brightness')
    #plt.ylim([0, 10000])
    plt.plot(hist)
    plt.savefig(path + 'image_' + str(hue_range) + '_bri.png',)

    # img = cv2.bitwise_and(hsv, hsv, mask=mask)
    img = cv2.bitwise_and(image, image, mask=mask)
    img = cv2.resize(img, (600, 400))
    cv2.imshow(str(hue_range), img)
    cv2.imwrite(path + 'image_' + str(hue_range) + '_aaa.png', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
