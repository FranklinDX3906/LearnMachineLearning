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

# 课时17 矩阵乘法
- 高中知识
- 编程简化计算

# 课时18 矩阵乘法特征
- 矩阵乘法符合结合律但是不符合交换律
- 单位矩阵加入之后矩阵乘法符合交换律（当是方矩阵时），如果不是方矩阵，交换后单位矩阵维度不同

# 课时19 逆和转置
- 求矩阵的逆一般使用软件
- 全0矩阵没有逆矩阵
- 奇异矩阵：没有逆矩阵

# 课时20 安装MATLAB并设置编程环境
- 安装即可，值得注意的是，MATLAB只限于本课程免费，而octave是开源的

# 课时21 安装MATLAB
- 方便起见安装了octave，所以未安装

# 课时22 在Windows上安装octave
- 不要安装4.0.0

# 课时23 在MacOSX上安装octave

# 课时24 在 Mac OS X (10.8 Mountain Lion and Earlier) 上安装 Octave

# 课时25 GNU/Linux 上安装 Octave

# 课时26 更多 Octave/MATLAB 资源

# 课时27 课件资料下载方法

# 课时28 多功能
- 多特特征决定最终结果（比方说房屋价格）
- n:特征数量
- 线性情况下使用多个参数
- 为了方便矩阵，设置为x0=1（x1开始是特征）
- 于是特征为n+1维的向量（x0开始，x0=1，x1到xn为特征）
- 下标表示不同的特征，上标表示不同的特征组
- 即为多元线性回归：h(x)=(A^T)X

# 课时29 多元线性回归
- 多元线性回归公式：

![](https://raw.githubusercontent.com/FranklinDX3906/LearnMachineLearning/master/learnMachineLearningBasic/MultivariateGradientReduction.png)

- 偏导的计算结果：

![](https://raw.githubusercontent.com/FranklinDX3906/LearnMachineLearning/master/learnMachineLearningBasic/MultivariateGradientReductionCalculation.png)

# 课时30 多元梯度下降法演练 I – 特征缩放
- 确保所有的特征值的尺度相当
- 将所有特征值的大小约束到-1与1之间是最好的，不过也不需要严格，相差不多即可，太小也不行
- 同时也可以使用归一化使得所有种类的特征值的所有平均值为0
- 特征缩放的主要目的是为了使得梯度下降更快

# 课时31 多元梯度下降法II – 学习率
- 主要讨论学习速率α
- 合适的学习速率坏使得每一步迭代之后代价函数的值都减小
- 代价函数收敛不一定非得在完全平才判断收敛，可以设置为“在一次迭代之后代价函数值下降小于某一个值θ则判断为收敛”，或者通过查看代价函数值与迭代次数的曲线
- 曲线还可以用于判断算法是否正常运行，如果代价函数逐渐变大，说明学习速率过大，起伏的曲线也可以使用减小学习速率的方法

# 课时32 特征和多项式回归
- 涉及到多项式的回归时，只需要把高次项替换为不一样的另一个一次的特征值即可

# 课时33 正规方程（区别于迭代方法的直接解法）
- 线性回归可以直接算出最优解（对每一个参数求偏导并置零）
- 或者直接使用公式计算：（X的每一行是一个样本）

![](https://raw.githubusercontent.com/FranklinDX3906/LearnMachineLearning/master/learnMachineLearningBasic/ParameterCalculationFormulafortheOptimalSolutionofMultipleLinearRegression.png)

- 无需特征缩放
- 优缺点：无需学习速率，无需迭代，但是特征种类很多时计算慢（O(N^3)）

# 课时34 正规方程在矩阵不可逆情况下的解决方法
- 矩阵不可逆时，pinv会计算出“伪逆”，最后依旧可以计算出正确结果
- 矩阵不可逆的情况主要是：特征互相相关（线性相关）；样本太少而特征太多
- 解决方法：看看有没有线性相关的特征；看看是不是样本太少特征太多，删掉一些特征，或者采用正则化

# 课时35 导师的编程小技巧
- 这一部分是提交代码的方式，应该是只开放给斯坦福上这门course的学生的

# 课时36 本章课程总结

# 课时37 课件资料下载方法

# 课时38 基本操作
- ~表示‘非’；&&表示‘与’；||表示‘或’
- PS1('xxx');可以更换提示符样式（XXX表示要更换成的样式）
- 加分号可以阻止打印输出
- A=[1,2;3,4;5,6],分号表示换行
- %表示注释
- 不加分号表示一组值，v=1;0.5;2表示v=[1,1.5,2]，中间的是
- ones(2,3)会生成一个2行3列的全是1的矩阵，zeros同理
- rand生成的都是0到1之间的数
- randn生成的服从高斯分布
- hist绘制直方图
- eye生成单位矩阵
- help+命令可以查看命令文档

# 课时39 移动数据
- size表示大小，length返回较大的那个维度
- pwd显示当前路径
- cd '' 切换位置，‘’之间输入切换到的路径
- ls 列出当前列表的文件
- load 加载文件
- who 显示当前所有的变量，whos显示变量细节
- save 2333.mat v %将v变量保存到2333.mat文件中
- clear清空所有变量
- save 2333.txt v -ascii %将变量存为ASCII码形式
- A(2,:)表示A矩阵的第二行所有元素
- A(:)将A中的所有元素放到一列（A本身不变）

# 课时40 计算数据
- A*B：矩阵相乘
- A.*B：对应元素相乘
- A.^2：乘方
- 1./A：求倒数
- exp：以e为底数
- abs：求绝对值
- A'：求A的转置
- max(A)：返回A每一列的最大值
- magic：返回幻方（每行每列每对角线之和相等）
- sum：求和；prod：求积；floor：向下取整；ceil：向上取整
- flipud：矩阵垂直翻转
- pinv：求矩阵的逆

# 课时41 数据绘制
- plot(横坐标，纵坐标)
- hold on：在原有图基础上继续画
- xlabel,ylabel,legend,title
- print -dpng ''：打印图片
- 使用figure(1);plot可以生成多个图片
- subplot：分割图像
- axis：设置横纵坐标范围
- clf清除图像，close关闭图像
- imagesc将矩阵可视化，colorbar图例,colormap gray，将矩阵可视化变为灰度可视化 
- 使用逗号连续调用函数

# 课时42 控制语句：for，while，if语句
- 后面加逗号表示循环内或判定内，end结束
- addpath添加路径
- 可以外部导入函数，前提是在路径内并保存为.m文件

# 课时43 矢量
- 使用向量內积描绘预测结果（参数矩阵的转置内乘X）
- 使用向量內积描绘参数更新，可以保证同步更新

# 课时44 本章课程总结

# 课时45 编程作业：线性回归