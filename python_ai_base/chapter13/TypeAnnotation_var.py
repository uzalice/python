"""
类型注解：变量
类型注解：在代码中涉及数据交互的地方，提供数据类型的注解（显式的说明）
"""
import json
import random
# 基础数据类型注解
var_1: int = 10
var_2: float = 3.1415926
var_3: bool = True
var_4: str = "hw"

# 类对象类型注解
class Student:
    pass

stu: Student = Student()

# 基础容器类型注解
# my_list: list = [1, 2, 3]
# my_tuple: tuple = (1, 2, 3)
# my_dict: dict = {"id": "111"}

# 容器类型详细注解
# 注意：元组类型设置详细注解，需要将每一个元素都标记出来，字典类型设置类型详细注解需要两个类型，分别是key和value
my_list: list[int] = [1, 2, 3]
my_tuple: tuple[str,int,bool] = ("hi",111,True)
my_dict: dict[str,str] = {"id": "111"}

# 在注释中进行类型注解
# 一般，无法直接看出变量类型之时会添加变量的类型注解
var_1 = random.randint(1, 10)   # type: int
var_2 = json.loads('{"name": "zhangsan"}')  # type: dict[str, str]
def func():
    return 10
var_3 = func()  # type: int
# 类型注解的限制
var_4: int = "itheima"
var_5: str = 123