import cv2
import numpy as np
import matplotlib.pyplot as plt

# Đọc ảnh gốc
image = cv2.imread('a.jpg', cv2.IMREAD_GRAYSCALE)  # Đọc ảnh xám

# Tạo ma trận hình dạng (3, 3)
window = np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]], np.float32)

# Lọc ảnh
filtered_image = cv2.filter2D(image, -1, window)

# Hiển thị ảnh gốc và ảnh đã lọc
plt.subplot(121)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.subplot(122)
plt.imshow(filtered_image, cmap='gray')
plt.title('Filtered Image')
plt.show()

# Lưu ảnh đã lọc
cv2.imwrite('Filtered Image.jpg', filtered_image)
