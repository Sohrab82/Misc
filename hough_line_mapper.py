import cv2
import numpy as np


def nothing(x):
    pass


def refresh_img(hmin, hmax, smin, smax, vmin, vmax):
    pass


def mousePosition(event, x, y, flags, param):
    pass


#cap = cv2.VideoCapture(0)
fname = "test.jpg"
image = cv2.imread(fname)
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image = cv2.Canny(image, 75, 200, 255)

cv2.namedWindow('image')

min_line_length_low = 1
min_line_length_high = image.shape[1]

max_line_gap_low = 1
max_line_gap_high = min_line_length_high

point_low = 1
point_high = 20

angle_low = 1
angle_high = 180

bin_size_low = 1
bin_size_high = image.shape[1] * 2

# create trackbars for color change
cv2.createTrackbar('point', 'image', point_low, point_high, nothing)
cv2.createTrackbar('angle', 'image', angle_low, angle_high, nothing)
cv2.createTrackbar('bin_size', 'image', bin_size_low, bin_size_high, nothing)
cv2.createTrackbar('min_line_length', 'image',
                   min_line_length_low, min_line_length_high, nothing)
cv2.createTrackbar('max_line_gap', 'image', max_line_gap_low,
                   max_line_gap_high, nothing)

while(True):
    # get trackbar positions
    point = cv2.getTrackbarPos('point', 'image') + 1
    angle = cv2.getTrackbarPos('angle', 'image') + 1
    bin_size = cv2.getTrackbarPos('bin_size', 'image') + 1
    min_line_length = cv2.getTrackbarPos('min_line_length', 'image') + 1
    max_line_gap = cv2.getTrackbarPos('max_line_gap', 'image')

    lines = cv2.HoughLinesP(image,
                            rho=point,
                            theta=angle * np.pi / 180,
                            threshold=int(bin_size),
                            minLineLength=int(min_line_length),
                            maxLineGap=int(max_line_gap))

    x = np.zeros(image.shape, dtype="uint8")
    if not lines is None:
        for line in lines:
            line = line[0]
            [x1, y1, x2, y2] = line
            cv2.line(x, (x1, y1), (x2, y2), (255, 255, 255), 1)
    cv2.imshow('image', x)
    print('------------------------')
    print(point)
    print(angle)
    print(bin_size)
    print(min_line_length)
    print(max_line_gap)

    k = cv2.waitKey(10) & 0xFF  # large wait time to remove freezing
    if k == 113 or k == 27:
        break


cv2.destroyAllWindows()
