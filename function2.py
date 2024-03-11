#function2.py

#가변인자(갯수가 정해져 있지 않은 입력을 처리하는 경우)
def union(*ar):
    res = []
    for item in ar:
        for x in item:
            if x not in res:
                res.append(x)
    return res



#람다 함수 정의
g = lambda x,y:x*y
print(g(2,3))
print(g(3,5))
print((lambda x:x*x)(3))
            