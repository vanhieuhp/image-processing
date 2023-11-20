import numpy as np
import cv2
import matplotlib.pyplot as plt

arr = np.ones(shape=(5, 5), dtype=np.uint8)
arr[0:3, 0:3] = 3
print(arr)
new_arr = cv2.cvtColor(arr, cv2.COLOR_BGR2RGB)
plt.imshow(arr, cmap="gray")
plt.show()
