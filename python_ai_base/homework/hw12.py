str = "万过薪月，员序程马黑来，nohtyP学"
reverse_str = str[::-1]
print(reverse_str) # 学Python，来黑马程序员，月薪过万
print(f"倒序切片：{reverse_str[9:14]}")
list = str.split("，")
print(list)
str1 = list[1]
str2 = str1.replace("来","")
print(f"split分隔，replace，倒序：{str2[::-1]}")