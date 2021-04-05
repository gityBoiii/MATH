def get_a_b(x1,y1,x2,y2) :
    from sympy import Symbol, solve
    a = Symbol('a')
    b = Symbol('b')
    ex1 = x1*a + b -y1
    ex2 = x2*a + b -y2
    print("ex1 : ", ex1)
    print("ex2 : ", ex2)
    ## a,b 구하기
    print(solve((ex1,ex2)))
    svd = solve((ex1,ex2))
    return svd