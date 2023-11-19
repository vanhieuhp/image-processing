import cv2
import numpy as np
import matplotlib.pyplot as plt

image_path = "/home/vanhieu/data/python/image-processing/images/girl.png"
image = cv2.imread(image_path, 0)


def show_image(img):
    # create figure
    fig = plt.figure(figsize=(10, 10))
    fig.add_subplot(111)
    plt.imshow(img, cmap="gray")

print(image.max())

ret, thresh1 = cv2.threshold(image, 120, 255, cv2.THRESH_TOZERO)
print(ret)

# show_image(image)
# show_image(thresh1)

cw_img = cv2.imread("/home/vanhieu/data/python/image-processing/images/ngu-van.jpg", 0)
show_image(cw_img)
ret, thresh2 = cv2.threshold(cw_img, 160, 255, cv2.THRESH_BINARY)

# cv2.imwrite("/home/vanhieu/data/python/image-processing/images/thresh.jpg", thresh2)
show_image(thresh2)

thresh3 = cv2.adaptiveThreshold(cw_img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 8)
show_image(thresh3)
plt.show()
