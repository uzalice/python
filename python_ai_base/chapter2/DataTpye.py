print("==========================")
# 数字类型Number
# 1.整数，浮点数 int float
a = 3
b = 3.14
print(a)
print(b)
print(type(a))
print(type(b))


print("==========================")
#2.布尔类型 bool
flag1 = True
flag2 = False
print(flag1)
print(flag2)
print(type(flag1))
print(type(flag2))

print("==========================")

# 3.复数 complex
c1 = 4 + 3j
print(c1) #(4 + 3j)
print(type(c1))


print("==========================")
# 字符串string类型
# string 的三种定义方式
str1 = 'hello world'
str2 =  "hello world"
str3 = """hello world"""
print(str1) # hello world
print(str2) # hello world
print(str3) # hello world

print(type(str1))
print(type(str2))
print(type(str3))

print("==========================")
# 列表 list 有序可变集合
nums = [1, 2, 3]
print(nums) # [1, 2, 3]
print(type(nums))

print("==========================")
# 元组 tuple 有序不可变集合
info = ("张三",20)
print(info) # ('张三', 20)
print(type(info))

print("==========================")
# 字典 dict 键值对集合
student = {"name":"李四","age":10}
print(student) #{'name': '李四', 'age': 10}
print(type(student))


print("==========================")
"""
类型检测函数
"""

# type()
age = 10
print(age)
print(type(age)) # <class 'int'>

# isinstance()
print(isinstance(age, int)) # True
print(isinstance(age, float)) # False