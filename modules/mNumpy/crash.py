import numpy as np

mylist = [1, 2, 3]

print(type(mylist))

my_array = np.array(mylist)

print(type(my_array))
print(np.arange(0, 10, 2))

print(np.zeros(shape=(10, 5)))

print(np.ones(shape=(2, 4)))

np.random.seed(101)
arr = np.random.randint(0, 100, 15)
print(arr)
print(arr.max())
print(arr.argmax())
print(arr.mean())
print(arr.shape)
print(arr.reshape(5, 3))

mat = np.arange(0, 100).reshape(10, 10)
print(mat)

row = 0
col = 1
print(mat[row, col])
print(mat[:, 1])
print(mat[:, 1].reshape(10, 1))
print(mat[2, :])
print(mat[0:3, 0:3])
mat[0:3, 0:3] = 0
print(mat)
new_mat = mat.copy()
print(new_mat)
new_mat[0:6, :] = 999
print(new_mat)
