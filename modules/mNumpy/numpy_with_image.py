import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

pic = Image.open("/images/my_dog.jpg")
# pic.show()

print(type(pic))

pic_arr = np.asarray(pic)
print(type(pic_arr))
print(pic_arr.shape)
# plt.imshow(pic_arr)
# plt.show()

pic_red = pic_arr.copy()
# plt.imshow(pic_red)
# plt.show()

# R G B
# RED CHANNEL VALUES 0 no red, pure black - 255 full pure red
# plt.imshow(pic_red[:, :, 0], cmap="gray") # Closer, more red
# plt.show()

pic_red[:, :, 2] = 0
plt.imshow(pic_red)
plt.show()
