import matplotlib.pyplot as plt
import numpy as np

r=float(input("r크기 입력 : "))

# th = np.arange(0,180, 1)
th = np.arange(0,360, 1)

#### x, y 모두 th로 구하기
x = r*(np.cos(np.radians(th)))
y = r*(np.sin(np.radians(th)))
x_s = np.arange(-1,2,1)

#### x는 범위, y는 피타고라스로
r = 300
x = np.arange(-r, r+1)
y = np.sqrt(r**2 - x**2)

# #확인
# for i in range(1,361,1):
#     print(i)
#     print(np.cos(np.radians(i)))

plt.plot(x+50,y-50)
plt.plot(x,-y)
plt.plot(x_s,x_s)
plt.scatter(0,0)
plt.axis("equal")
plt.grid(color="0.9")
plt.show()

