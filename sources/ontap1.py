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
if __name__ == "__main__":
    # Cau 1:
    def square(image):
        squared_img = np.square(image)
        return squared_img

    # Cau 2:
    def hist(image):
        histogram = np.zeros(256, dtype=int)
        for a in range(0, image.shape[0]):
            for b in range(0, image.shape[1]):
                histogram[image[a, b]] += 1
        cumulative_histogram = np.zeros(256, dtype=int)
        cumulative_histogram[0] = histogram[0]
        for i in range(1, 256):
            cumulative_histogram[i] = cumulative_histogram[i - 1] + histogram[i]
        mapping = ((cumulative_histogram - cumulative_histogram.min()) * 255 / (cumulative_histogram.max() - cumulative_histogram.min()))

        equalized_image = np.zeros_like(image)
        for a in range(0, image.shape[0]):
            for b in range(0, image.shape[1]):
                equalized_image[a, b] = mapping[image[a, b]]
        return equalized_image

    # Cau 3:
    def convolution(image, kernel):
        image_height, image_width = image.shape
        kernel_height, kernel_width = kernel.shape
        result = np.zeros_like(image)

        # Padding để xử lý các biên của ma trận ảnh
        padding_height = kernel_height // 2
        padding_width = kernel_width // 2
        padded_image = np.pad(image, ((padding_height, padding_height), (padding_width, padding_width)),
                              mode='constant')

        for i in range(image_height):
            for j in range(image_width):
                # Tính tổng giá trị phép nhân giữa bộ lọc và ma trận ảnh
                result[i, j] = np.sum(padded_image[i:i + kernel_height, j:j + kernel_width] * kernel)

        return result


    # Ma trận ảnh 8x8
    image = np.array([[3, 0, 1, 2, 7, 4, 1, 3],
                      [1, 4, 8, 2, 5, 6, 9, 3],
                      [2, 3, 4, 5, 5, 6, 7, 8],
                      [0, 1, 2, 3, 4, 5, 6, 7],
                      [6, 5, 4, 3, 2, 1, 0, 9],
                      [8, 7, 6, 5, 4, 3, 2, 1],
                      [9, 0, 1, 2, 3, 4, 5, 6],
                      [2, 3, 4, 1, 0, 5, 6, 7]])

    # Bộ lọc
    kernel = np.array([[1, 2, 1],
        [2, 4, 2],
        [1, 2, 1]])


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
    print(img_matrix[0:3, 0:3])

    img = cv2.filter2D(src=img_matrix, ddepth=-1, kernel=W)
    print(img)