import cv2
import numpy as np
import matplotlib.pyplot as plt


def load_image(filename):
    img = cv2.imread(filename).astype(np.float32) / 255
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img


def display_image(image):
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111)
    ax.imshow(image)

filename = "/home/vanhieu/data/python/image-processing/images/histogram.jpg"
image = load_image(filename)
# display_image(image)
# print(image)

gamma = 8
result = np.power(image, gamma)
# display_image(result)

image = load_image(filename)
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(image, text="BRICKS", org=(10, 150), fontFace=font, fontScale=6, color=(255, 0, 0), thickness=1)

kernel = np.ones(shape=(5, 5), dtype=np.float32) / 25
dst = cv2.filter2D(image, -1, kernel)

image = load_image(filename)
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(image, text="BRICKS", org=(10, 150), fontFace=font, fontScale=6, color=(255, 0, 0), thickness=1)
blurred = cv2.blur(image, ksize=(5, 5))

#  GAUSSIAN BLURRED
image = load_image(filename)
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(image, text="BRICKS", org=(10, 150), fontFace=font, fontScale=6, color=(255, 0, 0), thickness=1)
blurred_img = cv2.GaussianBlur(image, (5, 5), 10)

#  MEDIAN BLURRED
image = load_image(filename)
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(image, text="BRICKS", org=(10, 150), fontFace=font, fontScale=6, color=(255, 0, 0), thickness=1)
median_blurred = cv2.medianBlur(image, 5)
# display_image(median_blurred)

noise_image = cv2.imread("/home/vanhieu/data/python/image-processing/images/nature_noise.png")
noise_image = cv2.cvtColor(noise_image, cv2.COLOR_BGR2RGB)
display_image(noise_image)

denoise_image = cv2.medianBlur(noise_image,5)
display_image(denoise_image)

plt.show()