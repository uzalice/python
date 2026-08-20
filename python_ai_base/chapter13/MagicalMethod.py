"""
演示Python内置的各类魔术方法
"""
class Student:

    def __init__(self, name,age):
        self.name = name
        self.age = age

    # __str__魔术方法
    def __str__(self):
        return f"Student类对象，name:{self.name}, age:{self.age}"

    # __lt__魔术方法,小于、大于符号比较
    def __lt__(self, other):
        return self.age < other.age

    # __le__魔术方法
    def __le__(self, other):
        return self.age <= other.age

    # __eq__魔术方法
    def __eq__(self, other):
        print("你调用了__eq__()对吧")
        return self.age == other.age

stu1 = Student("周杰轮", 31)
stu2 = Student("林俊节", 36)
print(stu1)
print(stu1 == stu2)