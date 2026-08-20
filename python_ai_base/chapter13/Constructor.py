"""
构造器
 - 构建类对象的时候会自动运行
 - 构建类对象的传参会传递给构造方法，借此给成员变量复制
"""
class Student:
    # 有构造器，这里的属性可以省略
    # name = None
    # age = None
    # tel = None

    # 注意，这里的方法名是：__init__，前后都是两个下划线。
    def __init__(self, name, age, tel):
        self.name = name
        self.age = age
        self.tel = tel
        # print("创建了个学生对象")

stu = Student("周杰轮", 31, "18500006666")
print(stu.name)
print(stu.age)
print(stu.tel)
