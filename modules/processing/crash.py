import cv2
import matplotlib.pyplot as plt

filename = "/images/my_dog.jpg"
img = cv2.imread(filename)

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img = cv2.cvtColor(img, cv2.COLOR_RGB2HLS)
plt.imshow(img)
plt.show()