my_list = ['黑马程序员', '传智播客', '黑马程序员', '传智播客', 'itheima', 'itcast', 'itheima', 'itcast', 'best']
# 定义空集合
my_set = set()
# 通过for循环遍历列表，并将列表中的元素添加到集合中
for item in my_list:
    my_set.add(item)

# 最终得到去重后的集合对象，打印
for item in my_set:
    print(f"去重集合中的元素：{item}")