import matplotlib.pyplot as plt
import numpy as np
from sympy import Symbol, solve
from def_func import find_len

num1_len = find_len(num1 = float(input("자릿수 구할 숫자 입력 : ")))
print("num1_len : ", num1_len)


print ("1차 그래프 좌표 입력해")
x1 = float(input("x1 입력해 : "))
y1 = float(input("y1 입력해 : "))
x2 = float(input("x2 입력해 : "))
y2 = float(input("y2 입력해 : "))

## 중점 구하기
x_m = (x1 + x2)/2
y_m = (y1 + y2)/2
print(x1,":",y1,"|",x2,":",y2, "의 중점은 :", x_m, y_m)

a = Symbol('a')
b = Symbol('b')
ex1 = x1*a + b -y1
ex2 = x2*a + b -y2
print("ex1 : ", ex1)
print("ex2 : ", ex2)

ab = solve((ex1,ex2))
a = float(ab[a])
b = float(ab[b])
print("a,b의 값 : ", a,b)
print("방정식 : y = %.1fx + %.1f" %(a,b))
print("파란색은 1대1")

x = np.arange(1,11,1)
y = []
for i in range (0,10):
    y.append(a*x[i] + b)

# print(y)
plt.plot(x,y,marker='*',color="red")
plt.plot(x,x,marker='^',color="blue")
plt.axis('equal')
plt.grid()
plt.show()

