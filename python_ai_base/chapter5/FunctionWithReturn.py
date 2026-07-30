"""
函数返回值
"""

# 函数返回值的定义
def add(a,b):
    """
    :param a: 参数一
    :param b: 参数二
    :return: 返回值
    """
    return a+b

r = add(3,4)
print(r)

print("=================")

# None类型

def say_hello():
    print("hello")

#这种没有返回值而用变量来接收,打印出来是None,类型就是NoneType
result = say_hello()
print(result) # None
print(type(result)) # <class 'NoneType'>


"""
None的作用:
 - 用在函数无返回值上
 - 用在if判断上
    - 在if判断中None等同于False
    - 一般用于在函数中主动返回None,配合if判断做相关处理
 - 用于声明无内容的变量上
"""