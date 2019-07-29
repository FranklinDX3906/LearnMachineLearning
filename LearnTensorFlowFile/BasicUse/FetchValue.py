#coding:UTF-8

import tensorflow as  tf
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'



input1 = tf.constant(3.0)
input2 = tf.constant(2.0)
input3 = tf.constant(5.0)
intermed = tf.add(input2, input3)
mul = tf.multiply(input1, intermed)

with tf.compat.v1.Session() as sess:
    result = sess.run([mul, intermed])
    print(sess.run([mul, intermed]))

# 输出:
# [array([ 21.], dtype=float32), array([ 7.], dtype=float32)]