import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Task: Create a 5 by 5 array where every number is 10
matrix = np.ones(shape=(5,5))
matrix[:, :] = 10
print(matrix)
print("================================================")
# This line sets a "seed" so you get the same random numbers we do
np.random.seed(101)
arr = np.random.randint(low=0, high=100, size=(5, 5))

print(arr)
print(arr.max())
print(arr.min())

print("================================================")
pic = Image.open("/images/my_dog.jpg")
plt.imshow(pic)
plt.show()

print("================================================")
pic_arr = np.array(pic)
print(pic_arr.shape)
pic_red = pic_arr.copy()
# pic_red[:, :, 0] = 0
pic_red[:, :, 1] = 0
plt.imshow(pic_red)
plt.show()