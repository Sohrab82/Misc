import tensorflow as tf

print('**********************************')

# repeat a 2d array
x = tf.Variable([[1, 2, 3, 4], [5, 6, 7, 8]])
print('2D array: ', x, '\n----------------------------\n')
x = tf.repeat(x, repeats=2, axis=1)
print('Repeat along axis 1: ', x, '\n----------------------------\n')
x = tf.repeat(x, repeats=2, axis=0)
print('Repeat along axis 0: ', x, '\n----------------------------\n')

print('**********************************')

# repeat a 4dtensor
x = tf.random.normal((1, 2, 2, 1))
print('4D array 1x2x2x1: ', x, '\n----------------------------\n')
x = tf.repeat(x, repeats=2, axis=2)
print('Repeat along axis 2: ', x, '\n----------------------------\n')
x = tf.repeat(x, repeats=2, axis=1)
print('Repeat along axis 1: ', x, '\n----------------------------\n')
