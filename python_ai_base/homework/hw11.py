str = "itheima itcast boxuegu"
print(f"字符串中共存在：{str.count("it")}个it字符")
str1 = str.replace(" ","|")
print(f"字符串str中的空格被替换后结果为：{str1}")
my_list = str1.split("|")
print(f"字符串str1按照|进行分割后得到：{my_list}")