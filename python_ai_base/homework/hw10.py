stu_info = ("周杰伦",11,["football","music"])
print(f"年龄的下标为:{stu_info.index(11)}")
print(f"学生的姓名:{stu_info[0]}")
del stu_info[2][0]
print(stu_info)
stu_info[2].append("coding")
print(stu_info)