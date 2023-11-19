import numpy as np
import cv2
import matplotlib.pyplot as plt


def load_image():
    blank_image = np.zeros((600, 600))
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(blank_image, text="OpenCV", fontScale=5, org=(10, 300),
                fontFace=font, color=(255, 255, 255), thickness=10)
    return blank_image

def display_image(image):
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111)
    ax.imshow(image, cmap="gray")

blank_image = load_image()
display_image(blank_image)

plt.show()