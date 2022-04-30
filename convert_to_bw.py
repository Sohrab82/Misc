import cv2
import numpy as np
import os


img_filename = "test.jpg"
image = cv2.imread(img_filename)

print(image.shape)
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image = cv2.threshold(image, 210, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

img_rgb = np.ones([image.shape[0], image.shape[1], 3], dtype=np.int8) * 255
img_rgb[:, :, 0] = image
img_rgb[:, :, 1] = image
image = img_rgb

spl = os.path.splitext(img_filename)
cv2.imwrite(spl[0] + '_' + spl[1], image)
