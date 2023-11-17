import cv2
import numpy as np
import matplotlib.pyplot as plt

image_path = "/home/hieujr/data/python/image-processing/images/histogram.jpg"
image = cv2.imread(image_path, 0)

# fix_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# plt.imshow(image, cmap="gray")
# plt.show()

image_arr = np.array(image)
# Print the shape and content of the 'image_arr'
print("Image Shape:", image_arr.shape)
print("Image Content:\n", image_arr)

histo_arr = np.zeros(256, dtype=np.int32)

for i in range(image_arr.shape[0]):
    for j in range(image_arr.shape[1]):
        pixel_value = image_arr[i][j]
        histo_arr[pixel_value] += 1
print(histo_arr)

# write histogram
# fig, ax = plt.subplots(fixsize=(8, 6))
# ax.set_title("Histogram")

# ax.set_xlabel("X-Label")
# ax.set_ylabel("Y-Label")

plt.hist(histo_arr, bins='auto')
plt.title("Histogram")
plt.show()