import numpy as np
import random
import tensorflow.compat.v1 as tf

tf.disable_v2_behavior()

X_1 = tf.placeholder(tf.float32, name = "X_1")
X_2 = tf.placeholder(tf.float32, name = "X_2")

multiply = tf.math.multiply(X_1, X_2, name = "multiply")

with tf.Session() as session:
    result = session.run(multiply, feed_dict={X_1:[1,2,3], X_2:[4,5,6]})
    print(result)

x_input = np.random.sample((1,2))
print(x_input)

x = tf.placeholder(tf.float32, shape=[1,2], name = "X")
dataset = tf.data.Dataset.from_tensor_slices(x)
