"""
类与成员方法
"""

class people:
    name = None # 成员属性
    age = None

    def sayHello(self):
        print(f"hi,我是{self.name},今年{self.age}岁")

people1 = people() # self参数可以忽略不传
people2 = people()

people1.name =  "张三"
people1.age = 20
people1.sayHello()

people2.name = "李四"
people2.sayHello() # 这里不传参数就是None(定义类时的默认值)

class Clock:
    id = None
    price = None

    def ring(self):
        import winsound
        winsound.Beep(2000,3000)

# 构建2个闹钟对象并让其工作
clock1 = Clock()
clock1.id = "003032"
clock1.price = 19.99
print(f"闹钟ID：{clock1.id}，价格：{clock1.price}")
# clock1.ring()

clock2 = Clock()
clock2.id = "003033"
clock2.price = 21.99
print(f"闹钟ID：{clock2.id}，价格：{clock2.price}")
clock2.ring()
