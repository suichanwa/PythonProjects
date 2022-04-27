import tensorflow.compat.v1 as tf
import numpy as np
tf.disable_v2_behavior()


x = tf.placeholder(tf.float32, name="x")
y = tf.placeholder(tf.float32, name="y")
z = tf.multiply(x, y, name="z")
# Start the session to see the result, and pass values from the feed
with tf.Session() as session:
    print(session.run(z, feed_dict={x: 2.6, y: 2.0}))

tensor_2d = np.array(np.random.rand(4, 4), dtype='float32')
tensor_2d_1 = np.array(np.random.rand(4, 4), dtype='float32')
tensor_2d_2 = np.array(np.random.rand(4, 4), dtype='float32')

m1 = tf.convert_to_tensor(tensor_2d)
m2 = tf.convert_to_tensor(tensor_2d_1)
m3 = tf.convert_to_tensor(tensor_2d_2)

mat_product = tf.matmul(m1,m2)
mat_sum = tf.add(m2,m3)
mat_det = tf.matrix_determinant(m3)

with tf.Session() as session:
    print(session.run(mat_product))
    print(session.run(mat_sum))
    print(session.run(mat_det))