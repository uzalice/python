"""
演示JSON数据和Python字典的相互转换

json是一种轻量级的数据交互格式，采用完全独立于编程语言的文本格式来存储和表示数据（就是字符串）
Python语言使用JSON有很大优势，因为JSON无非就是一个单独的字典或一个内部元素都是字典的列表，所以JSON可以直接和Python的字典或列表进行无缝转换

事关两个方法：
 - json.dumps(data)，将python数据转换为json数据。在py里面是str
 - json.loads(json)，将json数据转换为python数据，在py里面是dict

注意：如果有中文可以带上：ensure_ascii = False参数来确保中文正常转换
"""
import json

# 准备符合json格式要求的python数据
data = {"name":"jack","age":20}
print(type(data)) # <class 'dict'>
# 1.通过json.dumps(data)方法把python数据转换为json数据
json_str = json.dumps(data)
print(type(json_str)) # <class 'str'>
print(json_str) # {"name": "jack", "age": 20}

# 通过json.loads(json)方法，把json数据转换为python数据
py_dict = json.loads(json_str)
print(type(py_dict)) # <class 'dict'>
print(py_dict) # {'name': 'jack', 'age': 20}
print("================================")

info_list = data = [{"name": "张大山", "age": 11}, {"name": "王大锤", "age": 13}, {"name": "赵小虎", "age": 16}]
print(type(info_list)) # <class 'list'>
print(info_list)
json_info_list = json.dumps(info_list) #
json_info_list = json.dumps(info_list, ensure_ascii=False) # 添加参数ensure_ascii=False使得中文正常显示
print(type(json_info_list)) # <class 'str'>
print(json_info_list)

py_info_list = json.loads(json_info_list)
print(type(py_info_list))
print(py_info_list)
