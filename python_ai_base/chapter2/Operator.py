"""
演示Python中的各类运算符
"""

# 算术运算符
print("1 + 1 = ",1 + 1)
print("2 - 1 = ",2 - 1)
print("3 * 3 = ",3 * 3)
print("4 / 2 = ",4 / 2) # 2.0，浮点数唉
print("5 / 2 = ",5 / 2) # 2.5，不会取整
print("11 // 2 = ",11 // 2) # 取整除
print("9 % 2 = ",9 % 2) # 取余
print("2 ** 3 = ",2 ** 3) # 指数运算

# 赋值运算符
num1 = 1 + 2 * 3
# 复合赋值运算符
# +=
num = 1
num += 1 # num = num + 1
print("num += 1: ", num)

num -= 1
print("num -= 1: ", num)

num *= 4
print("num *= 4: ", num)

num /= 2
print("num /= 2: ", num)

num = 3
num %= 2
print("num %= 2: ", num)

num **= 2
print("num **=2: ", num)

num = 9
num //= 2
print("num //= 2:", num)