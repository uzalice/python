"""
演示数据容器集合（set）的使用
 - 去重且无序
"""
my_set = {"传智教育", "黑马程序员", "itheima", "传智教育", "黑马程序员", "itheima", "传智教育", "黑马程序员", "itheima"}
print(f"my_set的内容:{my_set},类型是：{type(my_set)}")
empty_set = set()
print(f"empty_set的内容:{empty_set},类型是：{type(empty_set)}")

print("====================")

# 添加新元素
set1 = {"hello","world"}
set1.add("itheima")
print(set1) # {'itheima', 'world', 'hello'}

# 移除元素,set.remove(element)，移除指定元素
set1.remove("hello")
print(set1)

# 从集合中随机取出元素，同时这个元素也会被移出这个集合.set.pop()
element = set1.pop()
print(element)
print(set1)

# 清空集合,set.clear()
set1.clear()
print(set1)

print("====================")

# 取出两个集合的差集
# 集合1.difference(集合2),取出集合1和集合2的差集（集合1有而集合2没有的），得到一个新集合，集合1和集合2不变
set2 = {1,2,3}
set3 = {1,5,6}
set4 = set2.difference(set3)
print(set4)

# 消除两个集合的差集
# 语法：集合1.difference_update(集合2).功能：对比集合1和集合2，在集合1内，删除和集合2相同的元素。结果：集合1被修改，集合2不变
set2.difference_update(set3)
print(set2)
print(set3)

print("====================")

# 两个集合合并，求并集
# 语法：集合1.union(集合2).功能：将集合1和集合2组合成新集合。结果：得到新集合，集合1和几何2不变
set5 = set2.union(set3)
print(set5)

# 查看集合元素个数
print(f"集合set5的长度为：{len(set5)}")

# 遍历
for i in set5:
    print(i)

"""
集合特点：
 - 可以容纳多个数据
 - 可以容纳不同类型的数据
 - 数据是无序存储的（不支持下标索引）
 - 不允许重复数据存在
 - 可以修改（增加或删除元素）
 - 仅支持for循环
"""