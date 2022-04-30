import numpy as np

a = np.array([1, 2]).reshape(1, -1)
b = np.array([[1, 2, 3], [4, 5, 6]])

print('\nA:\n', a)
print('\nB:\n', b)

print('\na.shape:\n', a.shape)
print('\nb.shape:\n', b.shape)
print('\nnp.dot(a, b):\n', np.dot(a, b))
print('\nnp.multiply(a, b):\n', np.multiply(a, b))
print('\nnp.matmul(a, b):\n', np.matmul(a, b))
print('\na * b:\n', a * b)

print('--------')
b = np.array([3, 4]).reshape(1, -1)
print('\na.shape:\n', a.shape)
print('\nb.shape:\n', b.shape)
print('\nnp.dot(a, b):\n', np.dot(a, b.T))
print('\nnp.multiply(a, b):\n', np.multiply(a, b.T))
print('\nnp.matmul(a, b):\n', np.matmul(a, b.T))
print('\na * b:\n', a * b)
