"""
Created on Mon Oct 28 23:12:36 2019

@author: sohrab
"""
import cv2

video_filename = "test.MP4"


def show_image(title, image, width=300):
    r = width / float(image.shape[1])
    dim = (width, int(image.shape[0] * r))
    resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
    cv2.imshow(title, resized)


# construct the argument parser and parse the arguments
args = {}
args['source'] = 'cc.jpg'
args['target'] = 'aa.jpg'
args['output'] = 'oo.jpg'
args['clip'] = True
args['preservePaper'] = False

# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
cap = cv2.VideoCapture(video_filename)
source = cv2.imread(args["source"])

# Check if camera opened successfully
if (cap.isOpened() == False):
    print("Error opening video stream or file")

# Read until video is completed
while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        break
    show_image("Hello1", frame, 800)
    # Press Q on keyboard to  exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
