# 课时3 监督学习
- 监督学习两个问题：回归问题以及分类问题

# 课时4 无监督学习
- 无监督学习：输入数据集没有预先的标签
- 无监督学习主要内容：聚类算法

# 课时6 模型描述
- m：训练样本数；x：输入变量；y：输出值；(x,y)：一组样本；h：函数
- 房价：单变量线性回归，h_a(x) =a_00 +a_1x

# 课时7 代价函数
- 最小化

# 课时8 代价函数（一）
- 二元参数的代价函数可以使用等高线图表示

# 课时9 代价函数（二）

# 课时10 梯度下降
- 使用梯度下降法最小化代价函数
- 不同的起始点会得到不同的局部最优解
- 不同的参数需要同时进行更新，也就是说，第一次更新得到a0，a1，需要使用这个a0，a1计算应该得到的a0'和a1'而不是逐步更新，所以需要将计算值先赋值暂存才能在最后赋值给a0，a1
![正确和错误的赋值方式](https://github.com/FranklinDX3906/LearnMachineLearning/blob/master/learnMachineLearningBasic/SimultaneousUptade.png?raw=true)

# 课时11 梯度下降知识点总结

# 课时12 线性回归的梯度下降
- 如果学习速度合理，会逐渐逼近最优解
- 线性回归的代价函数是一个碗形的凸函数，所以局部最优解也是全局最优解
- 梯度下降公式的计算结果：
![计算公式](https://raw.githubusercontent.com/FranklinDX3906/LearnMachineLearning/master/learnMachineLearningBasic/LinearRegressionCalculation.png)

# 课时13 本章课程总结

# 课时14 矩阵和向量
- 除非特殊规定，否则向量从1开始计数
- n*1的矩阵可以看作是向量

# 课时15 加法和标量乘法
- 高中知识

# 课时16 矩阵向量乘法
- 高中知识
- 矩阵乘法用于编程时简化计算