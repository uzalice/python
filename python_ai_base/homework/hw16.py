"""
stu = Student("周杰轮", 31, "18500006666")
print(stu.name)
print(stu.age)
print(stu.tel)
"""
class Student:

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

for i in range(1,11):
    print(f"当前录入第{i}位学生信息，总共需要录入10位学生信息")
    name = input("请输入学生姓名：")
    age = input("请输入学生年龄：")
    address = input("请输入学生地址：")

    stu = Student(name, age, address)
    print(f"学生{1}的信息录入完毕，信息位：【学生姓名：{stu.name},年龄：{stu.age},地址：{stu.address}】")
