#DemoLoop.py

value = 5
while value > 0:
    print(value)
    value -= 1

#대부분 갯수가 정해져 있는 경우
lst = [100, 200, 300]
for item in lst:
    print(item)

fruit = {"apple":10, "banana":20, "kiwi":30}
for item in fruit.items():
    print(item)

print("key, value를 별도로 처리하는 경우")
for k,v in fruit.items():
    print(k,v)

print("---수열함수---")
for i in range(10):
    print(i)

print(list(range(1,11)))
print(list(range(2000,2025)))

print("---리스트 컴프리헨션(임베딩---")
lst = list(range(1,11))
print([i**2 for i in lst if i>5])

print("---필터링---")
def getBiggerThan20(i):
    return i>20

lst = [10, 25, 30]
itemL = filter(getBiggerThan20, lst)
for i in itemL:
    print(i)


print("---람다 함수 사용---")
itemL = filter(lambda x:x>20, lst)
for i in itemL:
    print(i)
    