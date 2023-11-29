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
])

image_height, image_width = image_matrix.shape
kernel_height, kernel_width = kernel.shape
filtered_image = np.zeros_like(image_matrix)

padding_height = kernel_height // 2
padding_width = kernel_width // 2
padded_image = np.pad(image_matrix, ((padding_height, padding_height), (padding_width, padding_width)), mode='constant')

for i in range(image_height):
    for j in range(image_width):
        filtered_image[i, j] = np.sum(padded_image[i:i + kernel_height, j:j + kernel_width] * kernel)

# Thực hiện phép tích chập
result = np.zeros((6, 6), np.uint8)
for i in range(6):
    for j in range(6):
        result[i, j] = np.sum(image_matrix[i:i + 3, j:j + 3] * kernel)

# Hiển thị ma trận ảnh gốc và ma trận ảnh đã lọc
print("\nMa trận lọc:")
print(kernel)

print("\nKết quả sau khi lọc:")
print(result)
