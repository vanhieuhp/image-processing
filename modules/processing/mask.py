import cv2
import numpy as np
import matplotlib.pyplot as plt

# Draw a rectangle
rectangle = np.zeros((300, 300), dtype=np.uint8)
print(rectangle)
cv2.rectangle(rectangle, (25, 25), (275, 275), 255, -1)
plt.imshow(rectangle, cmap="gray")
plt.show()

# Draw a circle
circle = np.zeros((300, 300), dtype=np.uint8)
cv2.circle(circle, (150, 150), 125, 255, -1)
plt.imshow(circle, cmap="gray")
plt.show()
# while True:
#     cv2.imshow("circle", circle)
#     if cv2.waitKey(1) & 0xFF == ord("q"):
#         break

bitwiseAnd = cv2.bitwise_not(rectangle, circle)
# cv2.imshow("AND", bitwiseAnd)
# cv2.waitKey(0)

plt.imshow(bitwiseAnd, cmap="gray")
plt.show()