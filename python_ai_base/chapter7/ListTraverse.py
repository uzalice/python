"""
list的遍历
 - while循环可以自定循环条件,并自行控制
 - for循环不可以自定循环条件,只可以一个个从容器内取出数据
"""

# 掌握while循环遍历列表
ages = [21, 25, 21, 23, 20]
index = 0
while index < len(ages):
    print(f"年龄为:{ages[index]}")
    index += 1
print("======================")

# 掌握for循环遍历列表
for age in ages:
    print(f"年龄为:{age}")