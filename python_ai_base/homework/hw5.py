"""
使用while循环打印一个九九乘法表
"""
i = 1
j = 1
while i < 10:
    while j <= i:
        print(f"{j} x {i} = {i * j}\t",end='')
        j += 1
    i += 1
    j = 1
    print()
