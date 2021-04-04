def find_len(num1):
    from math import floor
    result = []
    i=0
    num_flt = num1 - floor(num1)
    print("num1 : ", num1)
    print("정수 : ", floor(num1)) 
    print("num_flt : ", num_flt) #오류남. 밑의 자릿수 구하기를 따로 만들어, 자릿수만큼 floor(f1, -n) 할 것.
    while 1 :
        if num_flt < 0: #소숫점이면
            num_flt * 10
            i += 1
            if i > 1000: #너무 많이 반복하면
                result.append(i)
                print("소숫점 : ", i)
                break
        else:
            result.append(i)
            print("소숫점 : ", i)
            break
            
        
    i = 0
    while 1 :
        num1 = num1/10
        i += 1
        print("i는 : %d\nnum1은 : %f" %(i, num1))
        if int(num1) == 0:
            return i
        if i>1000:
            return i

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