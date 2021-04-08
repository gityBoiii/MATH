import matplotlib.pyplot as plt
import numpy as np
from sympy import Symbol, solve
from def_func import get_a_b

## 좌표 입력
print ("1차 그래프 좌표 입력해")
x1 = float(input("x1 입력해 : "))
y1 = float(input("y1 입력해 : "))
x2 = float(input("x2 입력해 : "))
y2 = float(input("y2 입력해 : "))

## 중점 구하기
x_m = (x1 + x2)/2
y_m = (y1 + y2)/2
print(x1,":",y1,"|",x2,":",y2, "의 중점은 :", x_m, y_m)

## 함수 기울기, 높이 구하기
svd = get_a_b(x1,y1,x2,y2)
print("svd :", svd) 
a = Symbol('a')
b = Symbol('b')   


# print(type(svd))
# print("a값 :",svd[a])
x = np.arange(-10, 10, 1)
y = svd[a]*x + svd[b]
y_s = x
## 수식 세워서? ㄴㄴ
# b_v = 
# y_v = -1/svd[a]*x + b_v
# if ~*x = 0, y_v = b_v, b_v = (0,~)
# y_v = (-1/svd[a])*x
## 특정 기울기의, 한점을 지나는 식의 b절편 구하기
# y_v = -1/svd[a]*x + b_v
b_v = y_m + 1/svd[a]*x_m
# print("b_v :",b_v)
y_v = -1/svd[a]*x + b_v

## 그래프 그리기
plt.plot(x,y)
plt.plot(x,y_s, color='0.9')
plt.plot(x,y_v)
plt.grid(color='0.5')
plt.axis('equal')
plt.scatter(x_m,y_m)
plt.show()

