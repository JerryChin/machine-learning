f = open('fev.txt', 'r')

ages = []
fev = []
for line in f:
 elements = line.strip().split(' ')
 if elements[0] == 'age':
     continue
 ages.append(elements[0])
 fev.append(elements[1])

# 声明 x 坐标值（年龄）
print("p=[" + ",".join(ages) + "]")

# 声明 y 坐标值 (肺活量）
print("q=[" + ",".join(fev) + "]")

# 绘制数据点（红色）
print("plot(x, y, '.r')")

# 设置坐标轴标签
print("xlabel(\"age\")")
print("ylabel(\"fev\")")
