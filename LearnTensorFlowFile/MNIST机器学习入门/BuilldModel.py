#coding:UTF-8

import tensorflow as tf
import tensorflow.examples.tutorials.mnist.input_data as input_data

import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

#导入数据
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

#我们通过操作符号变量来描述这些可交互的操作单元，x不是一个特定的值，
#而是一个占位符placeholder，我们在TensorFlow运行计算时输入这个值。
#我们希望能够输入任意数量的MNIST图像，每一张图展平成784维的向量。
x = tf.compat.v1.placeholder(tf.float32,[None,784])


#我们赋予tf.Variable不同的初值来创建不同的Variable：在这里，
#我们都用全为零的张量来初始化W和b。因为我们要学习W和b的值，它们的初值可以随意设置。
W = tf.Variable(tf.zeros([784,10]))
b = tf.Variable(tf.zeros([10]))

#这里x是一个2维张量拥有多个输入。然后再加上b，把和输入到tf.nn.softmax函数里面。
y = tf.nn.softmax(tf.matmul(x,W) + b)

#为了计算交叉熵，我们首先需要添加一个新的占位符用于输入正确值：
y_ = tf.compat.v1.placeholder("float", [None,10])

#首先，用 tf.log 计算 y 的每个元素的对数。接下来，我们把 y_ 的每一个元素和 tf.log(y) 
#的对应元素相乘。最后，用 tf.reduce_sum 计算张量的所有元素的总和。（注意，这里的交叉熵
#不仅仅用来衡量单一的一对预测和真实值，而是所有100幅图片的交叉熵的总和。对于100个数据点的预测
#表现比单一数据点的表现能更好地描述我们的模型的性能。
cross_entropy = -tf.reduce_sum(y_*tf.math.log(y))

#在这里，我们要求TensorFlow用梯度下降算法（gradient descent algorithm）
#以0.01的学习速率最小化交叉熵。梯度下降算法（gradient descent algorithm）
#是一个简单的学习过程，TensorFlow只需将每个变量一点点地往使成本不断降低的方向移动。
train_step = tf.compat.v1.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)
#TensorFlow在这里实际上所做的是，它会在后台给描述你的计算的那张图里面增加一系列新的
#计算操作单元用于实现反向传播算法和梯度下降算法。
#然后，它返回给你的只是一个单一的操作，当运行这个操作时，它用梯度下降算法训练你的模型，微调你的变量，不断减少成本。

#现在，我们已经设置好了我们的模型。在运行计算之前，我们需要添加一个操作来初始化我们创建的变量：
init = tf.compat.v1.global_variables_initializer()







#现在我们可以在一个Session里面启动我们的模型，并且初始化变量：
sess = tf.compat.v1.Session()
sess.run(init)

#然后开始训练模型，这里我们让模型循环训练1000次！
for i in range(1000):
    batch_xs, batch_ys = mnist.train.next_batch(100)
    sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})
#该循环的每个步骤中，我们都会随机抓取训练数据中的100个批处理数据点，然后我们用这些数据点作为参数替换
#之前的占位符来运行train_step。


correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))
#这行代码会给我们一组布尔值。为了确定正确预测项的比例，我们可以把布尔值转换成浮点数，然后取平均值。
#例如，[True, False, True, True] 会变成 [1,0,1,1] ，取平均值后得到 0.75.

accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
#最后，我们计算所学习到的模型在测试数据集上面的正确率。

print(sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))
