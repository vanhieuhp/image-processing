import numpy as np
import cv2

# Khởi tạo ma trận ảnh
image_matrix = np.array([[35, 24, 78, 89, 53, 68, 87, 34],
                         [46, 23, 57, 56, 46, 35, 23, 68],
                         [143, 15, 123, 46, 45, 35, 53, 56],
                         [224, 156, 231, 23, 65, 26, 68, 43],
                         [12, 167, 241, 45, 25, 46, 98, 75],
                         [42, 213, 124, 35, 57, 23, 65, 78],
                         [12, 21, 82, 28, 46, 65, 54, 46],
                         [53, 56, 28, 36, 27, 76, 89, 36]])

# Chuyển ma trận ảnh thành ảnh RGB
image_matrix = image_matrix.astype(np.uint8)
image = cv2.cvtColor(image_matrix, cv2.COLOR_GRAY2RGB)

# Hiển thị ảnh gốc
cv2.imshow("Original Image", image)
cv2.waitKey(0)

# Lưu ảnh sau khi chuyển thành ảnh RGB
cv2.imwrite("Original Image.jpg", image)
