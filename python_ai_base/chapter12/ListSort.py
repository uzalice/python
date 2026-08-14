"""
补充列表的sort方法-学习列表的sort方法来对列表进行自定义排序
"""
# 准备列表
my_list = [["a", 33], ["b", 55], ["c", 11]]

# 排序，函数
# def choose_sort_key(element):
#     return element[1]
# my_list.sort(key=choose_sort_key, reverse=True) # 按照第二个元素，降序
# print(my_list)

my_list.sort(key= lambda element:element[1],reverse=True)
print(my_list)