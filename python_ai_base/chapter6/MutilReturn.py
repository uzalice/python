"""
函数进阶教程-多个返回值
 - 按照返回值的顺序,写对应顺序的多个变量接收即可
 - 变量直接用逗号隔开
 - 支持不同类型的数据return
"""
# 多个返回值
def test_return():
    return 1,"我是字符串",True

x,y,z = test_return()
print(x) # 1
print(y) # 我是字符串
print(z) # True

def return_num():
    return 1
    return 2

a = return_num()
print(a) # 这里只会返回1