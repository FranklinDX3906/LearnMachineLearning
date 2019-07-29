# TensorFlow运作方式入门
本篇教程的目的，是向大家展示如何利用TensorFlow使用（经典）MNIST数据集训练并评估一个用于识别手写数字的简易前馈神经网络（feed-forward neural network）。我们的目标读者，是有兴趣使用TensorFlow的资深机器学习人士。

因此，撰写该系列教程并不是为了教大家机器学习领域的基础知识。

在学习本教程之前，请确保您已按照安装TensorFlow教程中的要求，完成了安装。

## 教程使用的文件
本教程引用如下文件：


文件  | 目的
--------------|------------------
mnist.py  |  构建一个完全连接（fully connected）的MINST模型所需的代码。
fully_connected_feed.py  |  利用下载的数据集训练构建好的MNIST模型的主要代码，以数据反馈字典（feed dictionary）的形式作为输入模型。

只需要直接运行fully_connected_feed.py文件，就可以开始训练：
>python fully_connected_feed.py

