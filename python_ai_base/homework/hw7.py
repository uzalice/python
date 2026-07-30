"""
1~100有多少偶数
"""
cnt = 0
for i in range(1,101):
    if i % 2 == 0:
        cnt += 1
print(cnt)