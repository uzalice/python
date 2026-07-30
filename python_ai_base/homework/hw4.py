"""
定义一个数字（1-10，随机产生），通过3次判断来猜出数字
 - 数字随机产生，范围1-10
 - 有三次机会猜测数字，通过三层嵌套判断实现
 - 每次猜不中，会提示大了或小了
"""
import random
num = random.randint(1, 10)

guess_num = int(input("请输入第一次要猜的数字（1~10）：\n"))

if guess_num == num:
    print("恭喜你，一次就猜对了")
else:
    if guess_num > num:
        print("你猜的偏大了")
    else:
        print("你猜的偏小了")
    guess_num = int(input("请输入第二次要猜的数字（1~10）：\n"))
    if guess_num == num:
        print("恭喜你，第二次猜对了")
    else:
        if guess_num > num:
            print("你猜的偏大了")
        else:
            print("你猜的偏小了")
        guess_num = int(input("请输入第三次要猜的数字（1~10）：\n"))
        if guess_num == num:
            print("恭喜你，第三次猜对了")
        else:
            print("抱歉，你没机会了")


