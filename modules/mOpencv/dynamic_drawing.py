import cv2
import numpy as np

# VARIABLES

# TRUE while mouse button Down, False while mouse button Up
drawing = False
ix = -1
iy = -1


# FUNCTION
def draw_rectangle(event, x, y, flags, params):
    global ix, iy, drawing

    if event == cv2.EVENT_LBUTTONDOWN:

        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img, (ix, iy), (x, y), -1)


# SHOWING THE IMAGE

# BLACK IMAGES
img = np.zeros(shape=(255, 255, 3))
cv2.namedWindow(winname="drawing")
cv2.setMouseCallback("drawing", draw_rectangle)

while True:
    cv2.imshow("drawing", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
