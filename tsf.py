import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

myConstant = tf.constant(4.5, name="firstconst", dtype=tf.float32)
myvar = tf.Variable(tf.zeros([1]), name="somevar", trainable=False)
xx = tf.constant(12.0, name="xx", dtype=tf.float32)
b = tf.constant(-2.0, name="yy", dtype=tf.float32)

yy = tf.Variable(tf.add(xx,b))


x = tf.placeholder(tf.float32, name="x")
y = tf.placeholder(tf.float32, name="y")
z = tf.multiply(x, y, name="z")

init = tf.compat.v1.global_variables_initializer()




with tf.Session() as session:
    session.run(init)
    print(session.run(z, feed_dict={xx: 2.6, yy: 2.0}))
    print(session.run(y))




