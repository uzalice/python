"""
通过Windows的文本编辑器，将下面内容，复制并保存到：word.txt，文件可以存储在任意位置
itheima itcast python
itheima python itcast
beijing shanghai itheima
shenzhen guangzhou itheima
wuhan hangzhou itheima
zhengzhou bigdata itheima

通过文件读取操作，读取此文件，统计itheima单词出现次数：6

"""

count = 0
with open("D:/word.txt","r",encoding="utf-8") as file:
    for line in file: # 这里的line类型是字符串，count()统计在字符串中字串出现次数
        count += line.count("itheima")
print(f"itheima单词出现次数：{count}")