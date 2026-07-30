"""
Python的七种数据类型
 - int
 - float
 - bool 布尔
 - str 字符串
 - list 列表
 - tuple 元组
 - dict 字典
"""

# 1.定义四个变量
name = "孙悟空"
age = 600
skill = ["筋斗云","72变"]
achievement = "大闹天宫"
print(name, age, skill, achievement)

# 2.定义变量c1 = "可乐" c2 = "牛奶" ,交换c1，c2
c1 = "可乐"
c2 = "牛奶"
print("c1 = ",c1,"c2 = ", c2)
c3 = c1
c1 = c2
c2 = c3
print("c1 = ",c1,"c2 = ", c2)

# python简洁写法
c3 = "123"
c4 = "456"
print("c3 = ",c3,"c4 = ", c4)
c3,c4 = c4,c3
print("c3 = ",c3,"c4 = ", c4)