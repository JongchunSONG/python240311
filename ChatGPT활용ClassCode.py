class Person:
    def __init__(self, person_id, name):
        self.id = person_id
        self.name = name

    def printInfo(self):
        print(f"ID: {self.id}, Name: {self.name}")


class Manager(Person):
    def __init__(self, person_id, name, title):
        super().__init__(person_id, name)
        self.title = title

    def printInfo(self):
        super().printInfo()
        print(f"Title: {self.title}")


class Employee(Person):
    def __init__(self, person_id, name, skill):
        super().__init__(person_id, name)
        self.skill = skill

    def printInfo(self):
        super().printInfo()
        print(f"Skill: {self.skill}")


# 테스트 코드
manager1 = Manager(101, "Manager One", "Senior Manager")
employee1 = Employee(201, "Employee One", "Python Developer")

manager2 = Manager(102, "Manager Two", "Project Manager")
employee2 = Employee(202, "Employee Two", "Data Scientist")

# Manager 객체 정보 출력
print("Manager 1 Info:")
manager1.printInfo()

print("\nManager 2 Info:")
manager2.printInfo()

# Employee 객체 정보 출력
print("\nEmployee 1 Info:")
employee1.printInfo()

print("\nEmployee 2 Info:")
employee2.printInfo()
