"""
封装
"""
class Student:
    name = None
    age = None
    # 以__开头的私有成员变量
    __height = None

    def __measure(self):
        self.__height = 180

    def info(self):
        self.__measure()
        print(f"个人信息：姓名：{self.name}，年龄：{self.age},身高：{self.__height}")

stu = Student()
stu.name = "张三"
stu.age = 29
stu.info()
