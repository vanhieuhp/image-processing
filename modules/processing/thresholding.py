import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("/home/hieujr/data/python/image-processing/images/rainbow.jpeg", 0)
plt.imshow(image, cmap="gray")
plt.show()
print(image.max())