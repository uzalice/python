"""
循环配合else使用
循环正常执行完,就会执行else里面的逻辑,这里的正常执行完即没有被break打断循环,continue不影响.
"""
for i in range(1,3):
    print(i)
else:
    print("循环正常结束")

print("===============")

for i in range(1,3):
    if i == 2:
        continue
else:
    print("循环正常结束")

print("===============")

for i in range(1,3):
    if i == 2:
        break
else:
    print("循环正常结束")