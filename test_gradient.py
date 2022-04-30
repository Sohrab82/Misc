import tensorflow as tf


def f(w1, w2):
    return 3 * w1 ** 2 + 2 * w1 * w2


# Now if you want to take derivatives of this function with respec to w1 and w2:

w1, w2 = tf.Variable(5.), tf.Variable(3.)
with tf.GradientTape() as tape:
    z = f(w1, w2)
gradients = tape.gradient(z, [w1, w2])
print(gradients)

x = tf.Variable(6.0, trainable=True)
with tf.GradientTape() as tape:
    y = x**3
print(tape.gradient(y, x).numpy())  # -> 108.0
