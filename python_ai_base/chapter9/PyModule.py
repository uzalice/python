"""
Python模块，是一个Python文件，以.py结尾，模块能定义函数、类、变量，模块内也能包含可执行代码

模块的导入
 语法：[from 模块名] import [模块|类|变量|函数|*] [as 别名]
 常见组合：
  - import 模块名
  - from 模块名 import 类、变量、方法等
  - from 模块名 import *
  - import 模块名 as 别名
  - from 模块名 import 功能名 as 别名

注意：当导入多个模块，且模块中有同名功能，当调用这个同名功能的时候，调用的是后面导入的模块的功能。
如果一个模块文件中有'__all__'变量，当使用'from xxx import *'导入时，只能导入这个列表中的元素
__all__ = [xxx,xxx]
"""

# import 模块名

# 导入time模块
# import time
# print("开始")
# 让程序休眠3秒（阻塞）
# time.sleep(3)
# print("结束")

# from 模块名 import 功能名

# from time import sleep
# print("开始")
# sleep(3)
# print("结束")

# from 模块名 import *

# from time import *
# print("开始")
# sleep(3)
# print("结束")


print("==========================")

# 自定义模块,每个python文件都可以作为一个模块，模块的名字就是文件的名字，也就是说自定义模块必须要符合命名规则。
from my_module import *
test(2,8)
