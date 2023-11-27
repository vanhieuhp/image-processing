import cv2
import matplotlib.pyplot as plt
import numpy as np

img_matrix = np.array([
    [35, 24, 78, 89, 53, 68, 87, 36],
    [46, 23, 57, 56, 46, 35, 23, 68],
    [143, 15, 123, 46, 45, 35, 53, 56],
    [224, 156, 231, 23, 65, 26, 68, 43],
    [12, 167, 241, 45, 25, 46, 98, 75],
    [42, 213, 124, 35, 57, 23, 65, 78],
    [12, 21, 82, 28, 46, 65, 54, 46],
    [53, 56, 28, 36, 27, 76, 89, 36],
])

# Task 1: Lấy bình phương các điểm ảnh của ma trận
square_image = np.square(img_matrix)
# square_image = np.zeros(shape=img_matrix.shape, dtype=np.uint16)
# print(test1)
for i in range(img_matrix.shape[0]):
    for j in range(img_matrix.shape[1]):
        square_image[i][j] = img_matrix[i][j] * img_matrix[i][j]

# print("Ma trận ban đầu: ")
# #
# print("=======================================")
# print("Ma trận bình phương: ")
# print(square_image)
# print(img_matrix)

# Task 2: Can bang histogram
hist_array = np.zeros(256, np.uint8)
for i in range(img_matrix.shape[0]):
    for j in range(img_matrix.shape[1]):
        hist_array[img_matrix[i][j]] += 1
# print(hist_array)
# plt.plot(hist_array)
# plt.show()

cumulative_sum = np.cumsum(hist_array)
cumulative_sum_normalized = (cumulative_sum - cumulative_sum.min()) * 255 / (
        cumulative_sum.max() - cumulative_sum.min())
equalized_image = np.interp(img_matrix.flatten(), np.arange(0, 256), cumulative_sum_normalized).reshape(
    img_matrix.shape)
# print(cumulative_sum)
# plt.imshow(img_matrix)
# plt.show()
# print("\nMa trận ảnh sau khi cân bằng histogram:")
# print(equalized_image)
# plt.imshow(equalized_image)
# plt.show()


# Task 3
kernel = np.array([
    [1, 2, 1],
    [2, 4, 2],
    [1, 2, 1]
])


def convolution(img, kernel):
    img_height, img_width = img.shape
    kernel_size = kernel.shape[0]
    output = np.zeros((img_height - kernel_size + 1, img_width - kernel_size + 1))

    for i in range(img_height - kernel_size + 1):
        for j in range(img_width - kernel_size + 1):
            output[i, j] = np.sum(img[i:i + kernel_size, j:j + kernel_size] * kernel)

    return output


kernel_image = convolution(img_matrix, kernel)

plt.imshow(kernel_image)
plt.show()
