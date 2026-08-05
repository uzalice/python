nums = [1,2,3,4,5,6,7,8,9,10]
"""
 - 遍历列表,取出列表内的偶数,并存入一个新的列表对象中
 - 使用while循环和for循环个操作一次
"""
index = 0
even_list1 = []
length = len(nums)

while index < length:
    num = nums[index]
    if num % 2 == 0:
        even_list1.append(num)
    index += 1

print(f"while循环中取出偶数得到新列表:{even_list1}")

even_list2 = []
for num in nums:
    if num % 2 == 0:
        even_list2.append(num)
print(f"for循环中取出偶数得到新列表:{even_list2}")