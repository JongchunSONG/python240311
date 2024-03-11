#ListDict.py
#Set 형식
a={1,2,3,3}
b={3,4,4,5}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

#Tuple 형식
tp = (10,20,30)
print(len(tp))

#함수 정의
def calc(a,b):
    return a+b, a*b

#호출
result = calc(3,4)
print(result)

print("id: %s, name: %s" %("kim", "김유신"))

#형식 변환
a = (1,2,3)
b = list(a)
b.append(4)
print(b)

#딕셔너리
fruits = {"apple":"red", "banana":"yellow"}
print(fruits)
print(fruits["apple"])

#입력
fruits["kiwi"] = "green"

#삭제
del fruits["apple"]
print(fruits)

#반복문
for item in fruits.items():
    print(item)
    