import cv2


def nothing(x):
    pass


fname = "test.jpg"
img_noblur = cv2.imread(fname)
img_noblur = cv2.resize(img_noblur.copy(), (600, 600))

mg_noblur = cv2.cvtColor(img_noblur, cv2.COLOR_BGR2GRAY)

img = img_noblur.copy()
img = cv2.blur(img_noblur, (7, 7))

canny_edge = cv2.Canny(img, 0, 0)

cv2.imshow('image', img)
cv2.imshow('canny_edge', canny_edge)

cv2.createTrackbar('min_value', 'canny_edge', 0, 255, nothing)
cv2.createTrackbar('max_value', 'canny_edge', 0, 255, nothing)

while(1):
    cv2.imshow('image', img)
    cv2.imshow('canny_edge', canny_edge)

    min_value = cv2.getTrackbarPos('min_value', 'canny_edge')
    max_value = cv2.getTrackbarPos('max_value', 'canny_edge')
    if min_value > max_value:
        t = min_value
        min_value = max_value
        max_value = t

    canny_edge = cv2.Canny(img, min_value, max_value, 255)

    k = cv2.waitKey(37)
    if k == 27:
        cv2.destroyAllWindows()
        break
