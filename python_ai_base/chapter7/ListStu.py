"""
python中的数据容器：
    一种可以容纳多份数据的数据类型，容纳的每一份数据称之为一个元素，每个元素可以是任意类型的数据

数据容器根据特点不同，如：
 - 是否支持重复元素
 - 是否可以修改
 - 是否有序，等

分别是list（列表），tuple（元组），str（字符串），set（集合），dict（字典）
"""


"""
列表的定义
注意：列表可以一次存储多个数据，且可以为不同的数据类型，支持嵌套
"""
name_list = ['Tom','Alice','Jack']
print(name_list) # ['Tom', 'Alice', 'Jack']
print(type(name_list)) # <class 'list'>

print('===========================')

#支持存储不同数据类型
mutil_list = [1,3,'Tom',True]
print(mutil_list)
# 嵌套定义
my_list = [[1,2,3],[4,5,6]]
print(my_list)
print(type(name_list)) # <class 'list'>
print(my_list[0][2])
print('===========================')

"""
列表的下标索引
列表中的每一个元素，都有其位置下标索引
语法：列表名[index]
"""

# 正向，从前向后的方向，从0开始，依次递增
print(name_list[0])
print(name_list[1])
print(name_list[2])

print('===========================')

# 反向，从后向前，从-1开始，依次递减
print(name_list[-1])
print(name_list[-2])
print(name_list[-3])

print('===========================')

"""
列表常用操作
 - 插入元素
 - 删除元素
 - 清空列表
 - 修改元素
 - 统计元素个数
"""
mylist = ["itcast", "itheima", "python"]

# 1.查找某元素的下标
# 功能：查找指定元素在列表的下标，如果找不到，报错ValueError
print(mylist.index("itcast")) # 0
#print(mylist.index("tom")) # ValueError: list.index(x): x not in list

print('===========================')

# 2.列表的修改功能
# 修改指定位置（索引）
mylist[1] = "lily"
print(mylist)

# 插入元素，插入指定索引处
mylist.insert(1,"Cpp")
print(mylist)

# 追加元素，添加到列表尾部
mylist.append("java")
print(mylist)
# 追加元素2,list1.extend(list2)，将list2中的内容取出，依次追加到list1尾部
add_list = [1,2,3]
mylist.extend(add_list)
print(mylist)

# 删除元素,语法: del list[index]
del mylist[1]
# 删除元素2,list.pop(index)
mylist.pop(0)
print(mylist)

# 删除某元素在列表中的第一个匹配项:list.remove(element)
mylist.append(2)
print(mylist)
mylist.remove(2)
print(mylist)

# 清空列表内容,list.clear()
add_list.clear()
print(add_list)

# 统计某元素在列表中的数量,list.count(element)
mylist.extend([2,2,2])
print(mylist)
print(mylist.count(2))

# 统计列表中有多少元素,len(list)
print(len(mylist))
print('===========================')


"""
列表特点:
 - 可以容纳多个元素,上限为2**63-1
 - 可以容纳不同数据类型的元素
 - 数据是有序存储的
 - 允许重复数据存在
 - 可以修改
"""
