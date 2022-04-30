import tensorflow as tf
import numpy as np


filter_size = 2
batch = 4
filter_per_channel = 2
num_channels = 3

inputs = tf.random.normal(
    [batch, filter_size, filter_size, num_channels], 0, 1, tf.float32)  # 2 filters
w = tf.random.normal([num_channels, filter_per_channel,
                     filter_size, filter_size], 0, 1, tf.float32)  # 2 filters
# print('w', tf.shape(w))
# print('X', tf.shape(X))


# def some_function(x, i):
#     return x + i
# a = tf.constant([[2, 1], [4, 2], [-1, 2]])
# a_rows = tf.expand_dims(tf.range(tf.shape(a)[0], dtype=tf.int32), 1)
# res, _ = tf.map_fn(lambda x: (some_function(x[0], x[1]), x[1]),
#                    (a, a_rows), dtype=(tf.int32, tf.int32))

@tf.function
def run_for_batch(x):
    def run_for_channel(ch_idx):
        tf.print('ch_idx:', ch_idx)
        ch = tf.cast(ch_idx, tf.int32)
        x_ch = x[:, :, ch]
        w_ch = w[ch, :, :, :]
        tf.print('X_CH', x_ch)

        def run_conv(w):
            return tf.reduce_sum(tf.multiply(x_ch, w))

        out_ch = tf.map_fn(run_conv, w_ch)
        tf.print('OUT_CH', out_ch)
        return out_ch

    ch_idxs = tf.range(num_channels, dtype=tf.float32)
    out_batch = tf.map_fn(run_for_channel, ch_idxs)
    tf.print(out_batch)
    return out_batch


# Out = tf.map_fn(run_for_batch, inputs)
# print('OUT', Out)
tf.print('-----\n', inputs[0, :, :, 1])
tf.print('-----\n', inputs[0, :, :, :])
y = inputs[0, 1, :, :] + inputs[1, :, :, :]
tf.print('-----\n', y)
