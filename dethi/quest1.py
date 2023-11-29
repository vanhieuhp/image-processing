import cv2
import numpy as np
import matplotlib.pyplot as plt

# Đọc ảnh gốc
image = cv2.imread('a.jpg', cv2.IMREAD_GRAYSCALE)

# Thiết lập ngưỡng
threshold1 = 85
threshold2 = 170
threshold3 = 255

# Tạo ma trận kết quả
result = np.zeros_like(image)

# Phân ngưỡng ảnh
result[(image >= threshold1 - 2) & (image <= threshold1 + 2)] = threshold1
result[(image > threshold1 + 2) & (image <= threshold2 - 2)] = threshold2
result[(image > threshold2 + 2) & (image <= threshold3 - 2)] = threshold3

# Hiển thị ảnh gốc và ảnh đã phân ngưỡng
plt.subplot(121)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.subplot(122)
plt.imshow(result, cmap='gray')
plt.title('Thresholded Image')
plt.show()

# Lưu ảnh đã lọc
cv2.imwrite('Thresholded Image.jpg', result)
