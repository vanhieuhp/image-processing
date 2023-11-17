import cv2
import matplotlib.pyplot as plt
import numpy as np

filename1 = "/home/hieujr/data/python/image-processing/images/my_dog.jpg"
filename2 = "/home/hieujr/data/python/image-processing/images/do-not-copy.jpg"

image1 = cv2.imread(filename1)
image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)

image2 = cv2.imread(filename2)
image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2RGB)

# plt.imshow(image2)
# plt.show()

print(image1.shape)
print(image2.shape)

# BLENDING IMAGES OF THE SAME SIZE
image1 = cv2.resize(image1, (1200, 1200))
image2 = cv2.resize(image2, (1200, 1200))

blended = cv2.addWeighted(src1=image1, alpha=0.8, src2=image2, beta=0.2, gamma=0)
# plt.imshow(blended)
# plt.show()

# OVERLAY SMALL IMAGE ON TOP OF A LARGER IMAGE (NO BLENDING)
# Numpy reassignment
image1 = cv2.imread(filename1)
image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)

image2 = cv2.imread(filename2)
image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2RGB)

image2 = cv2.resize(image2, (800, 600))
# plt.imshow(image2)
# plt.show()

large_image = image1
small_image = image2
x_offset = 0
y_offset = 0
x_end = x_offset + small_image.shape[0]
y_end = y_offset + small_image.shape[1]

large_image[x_offset:x_end, y_offset:y_end] = small_image
# plt.imshow(large_image)
# plt.show()

# MASK BLENDING
image1 = cv2.imread(filename1)
image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)

image2 = cv2.imread(filename2)
image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2RGB)

image2 = cv2.resize(image2, (600, 600))
x_offset = image1.shape[0] - image2.shape[0]
y_offset = image1.shape[1] - image2.shape[1]

rows, cols, channels = image2.shape
roi = image1[x_offset:image1.shape[0], y_offset:image1.shape[1]]
# plt.imshow(roi)
# plt.show()
image2gray = cv2.cvtColor(image2, cv2.COLOR_RGB2GRAY)
mask_inv = cv2.bitwise_not(image2gray)
# plt.imshow(mask_inv, cmap="gray")
# plt.show()
print(mask_inv.shape)

white_background = np.full(image2.shape, 255, dtype=np.uint8)
print("while backgroud:", white_background.shape)
bk = cv2.bitwise_or(white_background, white_background, mask=mask_inv)
print("bk:", bk.shape)
# plt.imshow(bk)
# plt.show()

# plt.imshow(mask_inv, cmap="gray")
# plt.show()

fg = cv2.bitwise_or(image2, image2, mask=mask_inv)
# plt.imshow(fg)
# plt.show()

final_roi = cv2.bitwise_or(roi, fg)
plt.imshow(final_roi)
plt.show()

large_image = image1
small_image = final_roi

large_image[x_offset:x_offset+small_image.shape[0], y_offset:y_offset+small_image.shape[1]] = small_image
plt.imshow(large_image)
plt.show()