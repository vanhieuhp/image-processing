import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("/images/my_dog.jpg")
print(type(img))

print(img.shape)
# plt.imshow(fix_img)
# plt.show()

# MATPLOT --> RGB: RED GREEN BLUE
# OPENCV --> BLUE GREEN RED
fix_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# plt.imshow(fix_img)
# plt.show()

img_gray = cv2.imread("/images/my_dog.jpg", cv2.IMREAD_GRAYSCALE)
# plt.imshow(img_gray, cmap='gray')
# plt.show()

print(fix_img.shape)
resize_image = cv2.resize(fix_img, (1000, 1000))
# plt.imshow(resize_image)
# plt.show()

w_ratio = 0.5
h_radio = 0.8
new_image = cv2.resize(fix_img, (0, 0), fix_img, w_ratio, h_radio)
# plt.imshow(new_image)
# plt.show()
# print(new_image.shape)

flip_img = cv2.flip(fix_img, -1)
# plt.imshow(flip_img)
# plt.show()

print(type(fix_img))
# cv2.imwrite("fix_img.jpg", fix_img)

fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111)
ax.imshow(fix_img)