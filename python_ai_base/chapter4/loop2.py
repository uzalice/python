"""
for循环初体验
 - 这里可以遍历字符串
"""

# 基础语法
name = "jack"
for x in name:
    print(x)

print("=================")
#range语句
"""
for 临时变量 in 待处理的数据集(可迭代对象)
    循环满足条件时执行的代码

 - 可迭代类型:其内容可以一个个一次取出来的类型,包括:
  - 字符串
  - 列表
  - 元组
  - 等等
"""
# range(num),这里是从0~num的数字,不包括num
for i in range(5): #0~4
    print(i)

print("=================")

# range(num1,num2),从num1~num2,不包括num2
for i in range(1,6):
    print(i)

print("=================")

# range(num1,num2,step),从num1~num2,不包括num2,这个step指的是每次每次增加step
for i in range(1,10,2):
    print(i) # 1,3,5,7,9

print("=================")
"""
变量作用域
"""
i = 0
for i in range(5):
    print(i) # 0,1,2,3,4

print(i) # 4

print("=================")

# 使用for循环来个九九乘法表,这个制表符还可以加载end里面,end='\t'
for i in range(1,10):
    j = 1
    for j in range(1,i + 1):
        print(f"{j} * {i} = {i * j}",end='\t')
    print()