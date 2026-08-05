"""
数据容器字典（Dict）
 - 使用{}存储原始，每一个元素是一个键值对
 - 每一个键值对包含key和value，使用冒号分隔
 - 键值对之间使用逗号隔开
 - key和value可以是任意类型的数据（key不可以是字典）
 - key不可以重复，重复会对原始数据进行覆盖
"""

# 字典的定义
stu_score = {"jack":99,"tom":90}
print(stu_score) # {'jack': 99, 'tom': 90}
print(stu_score["jack"]) # 99
print(stu_score["tom"]) # 90

print("=======================")

# 定义嵌套字典
stu_score_dict = {
    "王力鸿": {"语文": 77,"数学": 66,"英语": 33},
    "周杰轮": {"语文": 88,"数学": 86,"英语": 55},
    "林俊节": {"语文": 99,"数学": 96,"英语": 66}}

print(stu_score_dict)
print(f"王力鸿的各科成绩：{stu_score_dict["王力鸿"]}")

print("=======================")
# 字典的常用操作
# 1.新增元素
print(f"更新前的学生成绩{stu_score}")
stu_score["lily"] = 100
print(f"更新后的学生成绩{stu_score}")
# 2.更新元素，语法和新增一样，只不过key是已经存在的。

print("=======================")
# 3.删除元素，字典.pop(key)
stu_score.pop("lily")
print(f"删除lily前的成绩{stu_score}")
print(f"删除lily后的成绩{stu_score}")

# 4.清空字典，字典.clear()
stu_score.clear()
print(f"清空后的stu_score:{stu_score}")

# 5.获取全部的key
keys = stu_score_dict.keys()
print(f"stu_score_dict的所有key：{stu_score_dict.keys()}") # stu_score_dict的所有key：dict_keys(['王力鸿', '周杰轮', '林俊节'])

# 6.遍历字典
for key in keys:
    print(f"key={key},value={stu_score_dict[key]}")
    
# 7.获得键值对个数
print(len(stu_score_dict))