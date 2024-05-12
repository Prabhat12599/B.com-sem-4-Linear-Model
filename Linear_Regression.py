import numpy as np

x = np.array([28,41,40,38,35,33,46,32,36,33])
y = np.array([30,34,31,34,30,26,28,31,26,31])

def add (a):
    lenth = len(x)
    sum1 = sum(a)
    return sum1 / lenth

x1 = add(x)
print("x_bar =",x1)
y1 = add(y)
print("y_bar =",y1)
print()


def x_sub_ybar (a,b):
    sub = a - b
    return sub

x3 = x_sub_ybar(x, x1)
print("x-xbar",x3)
print("x-xbar =",(add(x3)))
print()

y3 = x_sub_ybar(y,y1)
# y31 = add(y3)
print("y-y bar", y3)
print("y-y bar =",(add(y3)))
print()

def power(a):
    squr = a * a
    return squr

squr_x = power(x3)
print("x-xbar_power ",squr_x)
print("x-xbar_power =",sum(squr_x))
print()

squr_y = power(y3)
print("x-xbar_power ",squr_y)
print("x-xbar_power =",sum(squr_y))
print()

x_mul_y = x3 * y3
print("x_mul_y", x_mul_y)
print("x_mul_y", sum(x_mul_y))
print()

# Regression
def regr(a,b):
    regression = a / b
    return regression
def a(a,b,c):
    a1 = a - b * c
    return a1

byx = regr(sum(x_mul_y), sum(squr_x))
print("byx =", byx)
a2 = a(y1,byx,x1)
print("a =",a2)
print()

bxy = regr(sum(x_mul_y), sum(squr_y))
print("byx =", bxy)

a1 = a(x1,bxy,y1)
print("a =",a1)
print()