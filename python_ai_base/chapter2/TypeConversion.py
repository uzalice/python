"""
字符串、整数、浮点数之间相互转换
用途
 - 从文件中读取的数字，默认是字符串，我们需要转换成数字类型
 - 后续学习的input()，默认结果是字符串，若需要数字也需要转换
 - 将数字转换成字符串可以写出到外部系统
"""

"""
int(x) 将x转换成一个整数
这个方法和type()一样，都是有返回值的，可以直接print()打印，或者使用变量存储
"""
a = "123"
print(a)
print(type(a)) # <class 'str'>
print(type(int(a))) # <class 'int'>
a1 = int(a)
print(a1)
print(type(a1)) # <class 'int'>

print("=============================")

# float(x) 将x转换成一个浮点数
b = "1.23"
print(b)
print(type(b)) # <class 'str'>
print(type(float(b))) # <class 'float'>
b1 = float(b)
print(b1)
print(type(b1)) # <class 'float'>

print("=============================")

# str(x) 将对象x转换成字符串
c = 123
d = 1.23
print(c)
print(d)
print(type(c)) # <class 'int'>
print(type(d)) # <class 'float'>
print(type(str(c))) # <class 'str'>
print(type(str(d)))  # <class 'str'>


print("=============================")

"""
类型转换注意事项
 - 任何类型都可以通过str()转换成字符串
 - 字符串内必须是数字才能使用int()或float()转换成数字
"""
v_str = "我是字符串"
# num = int(v_str) # ValueError: invalid literal for int() with base 10: '我是字符串'

"""
浮点数转换成整数，丢失精度（小数部分）
"""
num_float = 3.14
print(num_float) # 3.14
num_int = int(num_float)
print(num_int) # 3