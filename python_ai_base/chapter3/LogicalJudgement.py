"""
if 逻辑判断
 - 冒号
 - 四格缩进
"""
age = int(input("请输入你的年龄：\n"))
if age < 10:
    print("你是小学生。")
elif 10 <= age < 18:
    print("你是中学生")
else:
    print("你是大学生")