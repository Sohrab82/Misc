import tensorflow as tf


filter_size = 4  # size of input filters
batch = 3
filter_per_channel = 2
num_channels = 2
kernel_size = (3, 3)

# inputs = tf.random.uniform(\
#     [batch, filter_size, filter_size, num_channels], 0, 10, dtype=tf.int32) # 2 filters
# kernel = tf.Variable(tf.random.uniform(\
#     (kernel_size[0], kernel_size[1], num_channels, filter_per_channel), 0, 10, dtype=tf.int32))
inputs = tf.ones(
    [batch, filter_size, filter_size, num_channels], dtype=tf.int32)  # 2 filters
kernel = tf.Variable(tf.ones(
    (kernel_size[0], kernel_size[1], num_channels, filter_per_channel), dtype=tf.int32))

print('w', tf.shape(kernel))
print('X', tf.shape(inputs))

kernel = tf.cast(kernel, tf.float32)
inputs = tf.cast(inputs, tf.float32)


def call_me(inputs):
    Out = tf.squeeze(tf.nn.depthwise_conv2d(input=inputs, filter=kernel,
                     data_format='NHWC', strides=[1, 1, 1, 1], padding='VALID'))
    # Out = tf.reshape(Out, (-1, num_channels*filter_per_channel))
    return Out


# print('inputs', inputs)
print('inputs', tf.transpose(inputs, [0, 3, 1, 2]))
# print('kernel', kernel)
print('kernel', tf.transpose(kernel, [3, 2, 0, 1]))


bias = tf.random.uniform(
    [num_channels * filter_per_channel], 0, 10, dtype=tf.float32)  # 2 filters
Out = call_me(inputs)
print('bias', bias)
print('Out', Out.shape)
# Out = tf.nn.bias_add(Out, bias, 'N...C')
print('Out', Out)
# print(tf.transpose(Out, [0, 3, 1, 2]))
