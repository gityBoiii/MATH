import matplotlib.pyplot as plt
import numpy as np

# ## 수직 교차
# x = np.arange(-10, 11)
# y1 = 5*x + 5
# y2 = -1/5*x + 3

# plt.plot(x,y1,marker='*',color="red")
# plt.plot(x,y2,marker='*',color="blue")
# print("red : y1 = 5*x + 5")
# print("blue : y2 = -1/5*x + 3")
# plt.axis("equal")
# plt.grid(color="0.5")
# plt.show()

### 교점 찾기
x = np.arange(-10, 11)
y1 = 1/2*x + 2
y2 = -3/2*x + 6

plt.plot(x,y1,marker='*',color="red")
plt.plot(x,y2,marker='*',color="blue")
print("red : y1 = 1/2*x + 2")
print("blue : y2 = -3/2*x + 6")

## for문으로 해결
# print("x[5]는 : ", float(x[5]), type(float(x[5])))
for i in range(0,21,1):
    if y1[i] == y2[i]:
        print("교점은 ", x[i], ":", y1[i])

## solve함수로 해결
    # from sympy import Symbol,solve
    # x = Symbol("x")
    # y = Symbol("y")
    # ex1 = 1/2*x + 2 -y
    # ex2 = -3/2*x + 6 -y
    # print(solve((ex1,ex2)))

plt.axis("equal")
plt.grid(color="0.8")
plt.show()
