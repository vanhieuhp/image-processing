import cv2
import numpy as np
import matplotlib.pyplot as plt

# Đọc ảnh gốc
image = cv2.imread('a.jpg', cv2.IMREAD_GRAYSCALE)

# Cân bằng histogram
equalized_image = cv2.equalizeHist(image)

# Hiển thị ảnh gốc và ảnh đã cân bằng
plt.subplot(121)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.subplot(122)
plt.imshow(equalized_image, cmap='gray')
plt.title('Equalized Image')
plt.show()

# Lưu ảnh đã cân bằng
cv2.imwrite('Equalized Image.jpg', equalized_image)
