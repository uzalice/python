"""
使用for循环判断一个name中有多少"a"，itheima is a brand of itcast
"""
name = "itheima is a brand of itcast"
cnt = 0
for x in name:
    if x == "a":
        cnt += 1

print(f"itheima is a brand of itcast共有‘a’{cnt}个")