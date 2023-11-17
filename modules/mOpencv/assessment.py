import numpy as np
import cv2
import matplotlib.pyplot as plt

# TASK: Open image with correct RGB order
filename = "/images/my_dog.jpg"

image = cv2.imread(filename)
# while True:
#     cv2.imshow("Dog", image)
#     if cv2.waitKey(1) & 0xFF == ord("q"):
#         break
print(type(image))

fix_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
print(fix_image.shape)
# plt.imshow(fix_image)
# plt.show()

# TASK: Flip image
flip_image = cv2.flip(fix_image, -1)
# plt.imshow(flip_image)
# plt.show()

# TASK: Draw red rectangle
# x: (1200 -> 2000) , y: (500 -> 1250)
cv2.rectangle(fix_image, pt1=(1200, 500), pt2=(2100, 1350), color=(255, 0, 0), thickness=10)
# plt.imshow(fix_image)
# plt.show()

# TASK: Draw blue triangle
cv2.line(fix_image, pt1=(1200, 1350), pt2=(1650, 500), color=(0, 0, 255), thickness=20)
cv2.line(fix_image, pt1=(1650, 500), pt2=(2100, 1350), color=(0, 0, 255), thickness=20)
cv2.line(fix_image, pt1=(1200, 1350), pt2=(2100, 1350), color=(0, 0, 255), thickness=20)


# plt.imshow(fix_image)
# plt.show()

def draw_circle(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(resize_image, (x, y), 50, (0, 255, 0), 10)


resize_image = cv2.resize(fix_image, (1000, 1000))
cv2.namedWindow(winname="drawing")
cv2.setMouseCallback("drawing", draw_circle)
while True:
    cv2.imshow("drawing", resize_image)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()