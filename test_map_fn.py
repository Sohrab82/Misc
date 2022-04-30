import tensorflow as tf

def some_function(x, i):
    return x + i

a = tf.constant([[2, 1], [4, 2], [-1, 2]])
a_rows = tf.expand_dims(tf.range(tf.shape(a)[0], dtype=tf.int32), 1)
print(a)
print(a_rows)
res, _ = tf.map_fn(lambda x: (some_function(x[0], x[1]), x[1]), 
                   (a, a_rows), dtype=(tf.int32, tf.int32))

print(res)