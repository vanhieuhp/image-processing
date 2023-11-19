import cv2
import numpy as np
import matplotlib.pyplot as plt

image_path = "/home/vanhieu/data/python/image-processing/images/histogram.jpg"
image = cv2.imread(image_path, 0)

image_arr = np.array(image)
# Print the shape and content of the 'image_arr'
print("Image Shape:", image.shape)
# print("Image Content:\n", image_arr)

histo_arr = np.zeros(256, dtype=np.int32)

for i in range(image_arr.shape[0]):
    for j in range(image_arr.shape[1]):
        pixel_value = image_arr[i][j]
        histo_arr[pixel_value] += 1


def display_image(image):
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111)
    ax.imshow(image)
    plt.show()


image_path = "/home/vanhieu/data/python/image-processing/images/histogram.jpg"
image = cv2.imread(image_path)
fix_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# OPEN CV2 BGR
hist_values = cv2.calcHist([image], channels=[0], mask=None, histSize=[256], ranges=[0, 256])
print(hist_values.shape)
# plt.plot(hist_values)
# plt.show()

color = ['b', 'g', 'r']

# for i, col in enumerate(color):
#     histr = cv2.calcHist(image, channels=[i], mask=None, histSize=[256], ranges=[0, 256])
#     plt.plot(histr, color=col)
#     plt.xlim([0, 255])
#
# plt.title("Histogram for image")
# plt.show()

fig = plt.figure(figsize=(10, 7))


def show_image(image, stt, type):
    rows = 2
    columns = 2

    # Adds a subplot at the 1st position
    fig.add_subplot(rows, columns, stt)
    if type is not None and type == "gray":
        plt.imshow(image, cmap=type)
    else:
        # image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        plt.imshow(image)

    plt.axis('off')
    plt.title(f"Image {stt}")


mask = np.zeros(shape=(image.shape[:2]), dtype=np.uint8)
mask[50:150, 100:600] = 255

show_image(mask, 2, "gray")
show_image(fix_image, 1, None)

masked_image = cv2.bitwise_and(fix_image, fix_image, mask=mask)
show_image(masked_image, 3, "gray")

hist_mask_red = cv2.calcHist([image], channels=[2], mask=mask, histSize=[256], ranges=[0, 256])
hist_value = cv2.calcHist([image], channels=[2], mask=None, histSize=[256], ranges=[0, 256])
# plt.plot(hist_value)
# plt.title("hist mask value")
# plt.show()

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
show_image(gray_image, 1, "gray")

eq_hist = cv2.equalizeHist(gray_image)
show_image(eq_hist, 2, "gray")

# hist_values = cv2.calcHist([eq_hist], channels=[0], mask=None, histSize=[256], ranges=[0, 256])
# plt.plot(hist_values)
# plt.title("Hist value")
# plt.show()

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

print(hsv[:, :, 2].min())
hsv[:, :, 2] = cv2.equalizeHist(hsv[:, :, 2])
eq_color_image = cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB)
show_image(fix_image, 3, None)
show_image(eq_color_image, 4, None)
plt.show()