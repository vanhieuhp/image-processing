import cv2
import numpy as np

data = np.zeros([60, 60, 3])    #0: Blue, 1: Green, 2: Red - BGR >< RGB
h, w, c = data.shape

color_map = [
    (255, 0, 0), # blue
    (0, 255, 0), # green
    (0, 0, 255), # red
    (0, 0, 0), # black
    (255, 255, 255), # white
    (100, 100, 100), # grey
    (120, 50, 10),
    (36, 167, 227),
    (240, 212, 0),
]

assert h == w
step = h // 3
i = 0
for row in range(3):
    for col in range(3):
        data[row*step:(row+1)*step, col*step:(col+1)*step, :] = color_map[i]
        i += 1

# Điều chỉnh kích thước ảnh thành 300x300 pixel
resized_image = cv2.resize(data, (300, 300))

# Chuyển đổi từ BGR sang RGB
resized_image = resized_image.astype(np.uint8)
rgb_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB)

# Hiển thị ảnh
cv2.imshow("Create Image", rgb_image)
cv2.waitKey()

# Lưu ảnh có kích thước lớn hơn
cv2.imwrite("Create Image.png", rgb_image)