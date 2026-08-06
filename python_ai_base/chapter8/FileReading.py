"""
演示对文件的读取
"""

"""
open(name,mode,encoding)
 - name：要打开的目标文件名的字符串（可以包含文件所在的具体路径）
 - mode：设置打开文件的模式（访问模式）：只读、写入、追加等
    - r：以只读方式打开文件。文件的指针将会放在文件开头。默认是这个
    - w：打开一个文件只用于写入。如果该文件已存在则打开文件，从头开始编辑，原有内容会被删除。如果不存在，创建新文件
    - a：打开一个文件用于追加（如果文件不存在，则创建新文件进行写入）
 - encoding：编码格式（推荐使用UTF-8）
"""

# file = open("D:/python.txt","r",encoding="utf-8")
# print(type(file)) # <class '_io.TextIOWrapper'>

# 1.读取文件-文件对象.read(num)，指定字节长度
# print(f"读取10个字节的结果：{file.read(10)}")
# print(f"read方法读取全部内容的结果：{file.read()}") # 这里如果上面已经读完10字节，所以指针停留在第11字节，这里再全部读取就只能读取后面的内容。
print("==============================")

# 2.读取文件-文件对象.readline()读取一行
# print(f"readline()读取第一行的结果：{file.readline()}")
# print(f"readline()读取第二行的结果：{file.readline()}")

# 3.读取文件-文件对象.readlines()读取全部行，得到列表
# lines = file.readlines()
# print(type(lines)) # <class 'list'>
# print(f"file文件的内容：{lines}")

# 4.for循环读取文件，一次循环得到一行数据
# for line in file:
#     print(line)

# 5.关闭文件对象
# file.close()

# 6.with open() as f 通过with open打开文件，可以自动关闭
with open("D:/python.txt","r",encoding="utf-8") as file:
    for line in file:
        print(line)