"""
演示文件写入
"""

# # 1.打开文件，此时mode要设置为w
# file = open("D:/python.txt","w",encoding="utf-8")
# # 2.文件写入
# file.write("hello heima")
#
# # 3.内容刷新
# file.flush()

"""
 - 直接调用write()，内容并未写入文件，而是会积攒在程序的内存中，称之为缓冲区
 - 当调用flush()的时候，内容会真正写入文件
 - 这样做是避免频繁的操作硬盘，导致效率下降
 - 这时是w模式，所以会将原有内容清空，而填入write()的
"""

"""
演示文件的追加啊
"""


# 1.打开文件，此时mode要设置为w
file = open("D:/python.txt","a",encoding="utf-8")
# 2.文件写入
file.write("hello jack!")

# 3.内容刷新
file.flush()