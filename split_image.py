import cv2
import os
from imutils import resize

img_filename = "pic1.jpg"
image = cv2.imread(img_filename)
print(image.shape)

image = resize(image, width=630)
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image = cv2.threshold(image, 225, 255, cv2.THRESH_BINARY)[1]
print(image.shape)

n_r, n_c = image.shape
r_split = 3  # split rows into r_split segments
c_split = 2
for r in range(r_split):
    for c in range(c_split):
        segment = image[r * int(n_r / r_split):(r + 1) * int(n_r / r_split),
                        c * int(n_c / c_split):(c + 1) * int(n_c / c_split)]
        spl = os.path.splitext(img_filename)
        cv2.imwrite(spl[0] + '_' + str(r) + '_' + str(c) + spl[1], segment)
