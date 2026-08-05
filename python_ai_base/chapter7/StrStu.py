"""
字符串的常见操作

 - 字符串是一个无法修改的数据容器
"""

# 和其他数据容器一样,字符串也可以通过下标进行访问,正向从0开始,反向从-1开始
str1 = "itheima"
print(str1[0])
print(str1[-1])

print("======================")

# 查找特定字符串的下标索引值,str.index()
str2 = "itcast and itheima"
print(str2.index("and")) # 7,a的索引下标

print("======================")

# 字符串的替换,str1.replace(a,b)
"""
 - 语法:字符串.replace(字符串1,字符串2)
 - 功能:将字符串内的全部:字符串1,替换为字符串2
 - 注意:不是修改字符串本身,而是得到了一个新字符串
"""
name = "hello world"
new_name = name.replace("o","a")
print(new_name)
print(name)

print("======================")

# 字符串的分割
"""
 - 语法：字符串.split(分割符字符串)
 - 功能：按照指定的分隔符，将字符划分为多个字符串，并存入列表对象中
 - 字符串本身不变，而是得到了一个列表对象
"""
info = "Hello World"
info_list = info.split(" ") # 即按照空格分割这个字符串
print(info) # Hello World
print(type(info_list)) # <class 'list'>
print(info_list) # ['Hello', 'World']

print("======================")

# 字符串规整操作
# 字符串.strip()，去除前后空格
str3 = " hello world "
print(str3)
print(str3.strip())

# 字符串.strip(字符串)，去除前后指定字符串。比如这里传入11，末尾的1也会移除，因为这是按照单个字符移除
str4 = "11hello world21"
print(str4)
print(str4.strip("11"))

print("======================")

# 统计字符串中某字符串中出现次数,str.count()
str5 = "itcast and itheima"
print(str5.count("it"))

print("======================")

"""
    数字，字母，符号（包括空格），中文均算作一个字符
"""
# 统计字符串长度，len(字符串)
str6 = "1234 abcd !@#$ 我是汤姆"
print(len(str6)) #19

print("======================")

# while循环和for循环遍历字符串
str7 = "明日方舟"
index = 0
while index < len(str7):
    print(f"第{index+1}个字符为：{str7[index]}")
    index += 1

for i in str7:
    print(i)

"""
字符串特点：
 - 长度任意（取决于内存大小）
 - 支持索引访问
 - 允许重复字符串存在
 - 不可以修改
 - 支持for循环
"""