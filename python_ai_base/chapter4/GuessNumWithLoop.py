"""
使用while循环优化的猜数字游戏
"""
import random
num = random.randint(1,100)

cnt = 1
flag = True

while flag:
    guess_num = int(input("请输入猜测数字：\n"))
    if guess_num == num:
        print(f"猜对了，共计猜了{cnt}次")
        flag = False
    else:
        if guess_num > num:
            print("大了")
        else:
            print("小了")
    cnt += 1