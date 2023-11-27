import numpy as np
import cv2
import matplotlib.pyplot as plt
from PIL import Image
# Giả sử img_matrix là ma trận ảnh của bạn, đây là một ví dụ ma trận ảnh 3x3
img_matrix = np.array([
    [35,24,78,89,53,68,87,36],
    [46,23,57,56,46,35,23,68],
    [143,15,123,46,45,35,53,56],
    [224,156,231,23,65,26,68,43],
    [12,167,241,45,25,46,98,75],
    [42,213,124,35,57,23,65,78],
    [12,21,82,28,46,65,54,46],
    [53,56,28,36,27,76,89,36],
])

# Lấy bình phương của các điểm ảnh trong ma trận ảnh
squared_img = np.square(img_matrix)

# Hiển thị ma trận ảnh ban đầu và ma trận ảnh đã bình phương
print("Ma trận ảnh ban đầu:")
print(img_matrix)

print("\nMa trận ảnh đã bình phương:")
print(squared_img)

histogram, _ = np.histogram(img_matrix.flatten(), bins=256, range=(0,256))

# Tính toán cân bằng histogram
cumulative_sum = np.cumsum(histogram)
cumulative_sum_normalized = (cumulative_sum - cumulative_sum.min()) * 255 / (cumulative_sum.max() - cumulative_sum.min())
equalized_image = np.interp(img_matrix.flatten(), np.arange(0, 256), cumulative_sum_normalized).reshape(img_matrix.shape)

print("\nMa trận ảnh sau khi cân bằng histogram:")
print(equalized_image)

W = np.array([
    [1, 2, 1],
    [2, 4, 2],
    [1, 2, 1]
])

# Thực hiện phép tích chập
result = np.zeros((6, 6))  # Kích thước ma trận kết quả sau khi lọc
for i in range(6):
    for j in range(6):
        result[i, j] = np.sum(img_matrix[i:i+3, j:j+3] * W)

# Hiển thị ma trận ảnh gốc và ma trận ảnh đã lọc

print("\nMa trận lọc:")
print(W)

print("\nKết quả sau khi lọc:")
print(result)