"""
匿名函数
 - 函数作为参数传递
 - lambda匿名函数
"""

"""
 - 函数本身是可以作为参数传入另一个函数中进行使用的
 - 将函数传入的作用在于：传入计算逻辑，而非数据
"""

# 函数作为参数传递
def test_fun(compute):
    result = compute(2,5)
    return result

def compute(a,b):
    # return a + b
    return a - b

print(test_fun(compute))


"""
匿名函数定义语法：
lambda 传入参数：函数体（一行代码）
 - lambda是关键词，表示定义匿名函数
 - 传入参数表示匿名函数的形式参数，如：x，y表示接收两个形式参数
 - 函数体，就是函数的执行逻辑，要注意：只能写一行，不能写多行代码
"""

def test_func(compute):
    result = compute(1,3)
    print(result)

test_func(lambda x,y: x * y)