import numpy as np
import cv2
import matplotlib.pyplot as plt

# CAU 1
# Khởi tạo ma trận ảnh
image_matrix = np.array([[35, 24, 78, 89, 53, 68, 87, 34],
                         [46, 23, 57, 56, 46, 35, 23, 68],
                         [143, 15, 123, 46, 45, 35, 53, 56],
                         [224, 156, 231, 23, 65, 26, 68, 43],
                         [12, 167, 241, 45, 25, 46, 98, 75],
                         [42, 213, 124, 35, 57, 23, 65, 78],
                         [12, 21, 82, 28, 46, 65, 54, 46],
                         [53, 56, 28, 36, 27, 76, 89, 36]])

fig = plt.figure(figsize=(10, 7))

darkened_image = np.zeros(image_matrix.shape[:2])
for i in range(image_matrix.shape[0]):
    for j in range(image_matrix.shape[1]):
        darkened_image[i][j] = image_matrix[i][j] - 150

print(image_matrix)
print(darkened_image)
fig.add_subplot(2, 2, 1)
plt.imshow(darkened_image)
plt.axis('off')
plt.title("CAU 1")

# CÂU 2: Cân bằng histogram ảnh
hist_array = np.zeros(256, np.uint8)
for i in range(image_matrix.shape[0]):
    for j in range(image_matrix.shape[1]):
        hist_array[image_matrix[i][j]] += 1

cumulative_sum = np.cumsum(hist_array)
cumulative_sum_normalized = (cumulative_sum - cumulative_sum.min()) * 255 / (
        cumulative_sum.max() - cumulative_sum.min())
equalized_image = np.interp(image_matrix.flatten(), np.arange(0, 256), cumulative_sum_normalized).reshape(
    image_matrix.shape)

print(cumulative_sum)
print("\nMa trận ảnh sau khi cân bằng histogram:")
print(equalized_image)

fig.add_subplot(2, 2, 2)
plt.imshow(equalized_image)
plt.axis('off')
plt.title("CAU 2")

# CAU 3
kernel = np.array([
    [1, 1, 1],
    [1, 8, 1],
    [1, 1, 1]
], dtype="float")

result_matrix = np.zeros_like(image_matrix)

for i in range(1, image_matrix.shape[0] - 1):
    for j in range(1, image_matrix.shape[1] - 1):
        window = image_matrix[i-1:i+2, j-1:j+2]
        result_matrix[i, j] = np.sum(kernel * window)

# In kết quả
print(result_matrix)

fig.add_subplot(2, 2, 3)
plt.imshow(result_matrix)
plt.axis('off')
plt.title("CAU 3")

plt.show()