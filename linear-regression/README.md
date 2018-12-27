

由于我们处于入门阶段，所以使用[这里](https://newonlinecourses.science.psu.edu/stat462/node/101/) 提供的数据示例 2 作为训练数据，文件名为 fev.txt。

第一步执行 read.py 提取年龄和呼气量数据，形成数据点然后作图。

第二步建立模型，找出我们的代价函数，这里我们选用平方误差代价函数。

J(theta_0, theta_1) = 1/(2m) * sum_(i=1)^m [h_theta(x^i) - y^i]^2


求 J 的梯度 grad J(theta_0, theta_1) = 

∂J/∂theta_0 = 1/m * sum_(i=1)^m [(h_theta(x^i) - y^i)]
∂J/∂theta_1 = 1/m * sum_(i=1)^m [(h_theta(x^i) - y^i)x1(i)]

theta_0 = theta_0 - ∂J/∂theta_0
theta_1 = theta_1 - ∂J/∂theta_1
theta 0: 0.716405 theta 1: 0.195675

最终求得假设函数为：
y = 0.716405 + 0.195675 * x



07,3301
06,1540
05,601
04,285
03,409
02,534
01,611
00,1079
23,2312
22,3379
21,4140
20,4732
19,5048
18,5100
17,4806
16,4277
15,3841
14,3932
13,4356
12,3907
11,4228
10,4271
09,4253
08,4105


#### 其它
* [训练数据](http://archive.ics.uci.edu/ml/datasets.html?area=&att=&format=&numAtt=&numIns=&sort=attup&task=reg&type=&view=table)
