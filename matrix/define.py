import numpy as np
from sympy import Symbol, solve

""" 매트릭스 만들기 """
# 정의
m1 = np.matrix(
    [
        [5,10],
        [11,3]
    ]
)
m2 = np.matrix([[6,11], [12,4]])
stM = np.matrix(
    [
        [1,0],
        [0,1]
    ]
)

# 역함수
def revMatrix (m2):
    ## 요소 변수에 저장  
    a1 = m2[0,0]
    a2 = m2[0,1]
    a3 = m2[1,0]
    a4 = m2[1,1]   
    print("a1, a2, a3, a4 : ", a1, a2, a3, a4)
    ## 역함수로 변환
    revM = np.matrix(
        [
            [-a4,a2],
            [a3,-a1]
        ]
    )
    return revM

# .
# [ x1, x2 ]  ->
# [ x3, x4 ]  
# <-      .


# m2_rev = np.linalg.inv(m2) #오작동
print("m2의 역행렬 : ", revMatrix(m2))
revM = revMatrix(m2)
print("testing : ", m2*revM)

# 출력
print("m1 : \n", m1)
print("m2 : \n", m2)
print("m1 + m2 : \n", m1+m2)
print("기존의 50%만 : \n", m1/2)
print("m1 * m2 : \n", m1*m2)
# print("m2의 역: \n", m2_rev)
# print("m2 * m2_rev: \n", m2*m2_rev)
print("단위행렬 연산 : \n", m2*stM)

