import time

f = open('fev.txt', 'r')

ages = []
fev = []
for line in f:
    elements = line.strip().split(' ')
    if elements[0] == 'age':
        continue
    ages.append(int(elements[0]))
    fev.append(float(elements[1]))


def gradient(theta0, theta1, ages, fev):
    time.sleep(0.01)
    m = len(ages)
    new_theta0 = theta0 - 0.001 * ( _sum(theta0, theta1, ages, fev) / m)
    new_theta1 = theta1 - 0.001 * (_sum2(theta0, theta1, ages, fev) / m)

    print("theta 0: %f theta 1: %f" % (new_theta0, new_theta1))
    gradient(new_theta0, new_theta1, ages, fev)

    return 0

def _sum(theta0, theta1, ages, fev):

    m = len(ages)

    summation = 0
    for index in range(m):
        summation += ((theta0 + theta1 * ages[index]) - fev[index]) # 假设函数 h(x) = theta0 + theta0 * x

    return summation

def _sum2(theta0, theta1, ages, fev):

    m = len(ages)
    print("ages: %d" % m)

    summation = 0
    for index in range(m):
        summation += (((theta0 + theta1 * ages[index]) - fev[index]) * ages[index]) # 假设函数 h(x) = theta0 + theta0 * x

    return summation

gradient(1, 3, ages, fev)