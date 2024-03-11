#Person.py

#1)클래스 정의
class Person:
    #초기화 매서드
    def __init__(self):
        self.name = "default name"
    def print(self):
        print("My name is {0}".format(self.name))

#2)인스턴스를 생성
p1 = Person()
p1.print()
