"""
tuple元组的定义和操作
 - 元组一旦定义,就不可修改,所以当我们需要在程序内封装数据,又不希望封装的数据被篡改,那么元组就非常合适了
 - 定义元组使用小括号,且使用逗号隔开各个数据,数据可以是不同的数据类型,元组也支持嵌套
"""

# 元组的定义
t1 = (1, "Hello", True)
t2 = ()
t3 = tuple()
print(f"t1的类型是：{type(t1)}, 内容是：{t1}")
print(f"t2的类型是：{type(t2)}, 内容是：{t2}")
print(f"t3的类型是：{type(t3)}, 内容是：{t3}")

print("====================")

my_tuple = (1,True,"tom")
print(type(my_tuple))
print(my_tuple)

print("====================")

# 元组只有一个数据,这个数据后面要添加逗号
test_tuple = ('hello')
print(type(test_tuple)) # <class 'str'>
print(test_tuple) # <class 'str'>

t4 = ("hello", )
print(f"t4的类型是：{type(t4)}, t4的内容是：{t4}")

print("====================")

"""
元组的操作:
 - index(element)
 - count(element)
 - len(tuple)
"""

# 1.index查找方法
t6 = ("传智教育", "黑马程序员", "Python")
index = t6.index("黑马程序员")
print(f"在元组t6中查找黑马程序员，的下标是：{index}")
# 2.count统计方法
t7 = ("传智教育", "黑马程序员", "黑马程序员", "黑马程序员", "Python")
num = t7.count("黑马程序员")
print(f"在元组t7中统计黑马程序员的数量有：{num}个")
# 3.len函数统计元组元素数量
t8 = ("传智教育", "黑马程序员", "黑马程序员", "黑马程序员", "Python")
num = len(t8)
print(f"t8元组中的元素有：{num}个")

print("====================")

# 元组的遍历：while
index = 0
while index < len(t8):
    print(f"元组的元素有：{t8[index]}")
    # 至关重要
    index += 1

# 元组的遍历：for
for element in t8:
    print(f"2元组的元素有：{element}")


# 定义一个元组
t9 = (1, 2, ["itheima", "itcast"])
print(f"t9的内容是：{t9}")
t9[2][0] = "黑马程序员"
t9[2][1] = "传智教育"
print(f"t9的内容是：{t9}")
