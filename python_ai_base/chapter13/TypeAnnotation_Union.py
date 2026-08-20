"""
演示Union联合类型注解
注意：需要导包。
from typing import Union
Union联合类型注解，在变量注解、函数（方法）形参和返回值注解中均可使用
"""

from typing import Union

my_list: list[Union[int, str]] = [1, 2, "111"]
my_dict: dict[str, Union[int, str]] = {"name":"张三","age":10}
print(my_list)
print(my_dict)