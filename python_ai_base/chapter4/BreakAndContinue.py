"""
这个没什么好说的,用一个案例来解决这一章吧
"""
import random
total = 10000
for i in range(1,21):
    score = random.randint(1,10)
    if  score < 5:
        print(f"{i}号员工绩效:{score},不能給奖金")
        continue
    else:
        if total <= 0:
            print("奖金不够了,下次再发吧")
            break
        else:
            print(f"{i}号员工得到1000元奖金")
            total -= 1000