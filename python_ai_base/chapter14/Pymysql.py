"""
第三方库：pymysql完成对mysql数据库的操作。
pip install pymysql
"""

from pymysql import Connection, connect

connection = Connection(
    host="localhost", # 主机
    port=3306, # 端口
    user="root", # 用户
    password="itheima", # 密码
    autocommit=True # 密码自动提交
)
# 获取数据库消息
print(connection.get_server_info()) # 8.0.26

# 执行非查询性质sql
cursor = connection.cursor() # 获取到游标对象
# 选择数据库
connection.select_db("itheima")
# 执行sql
cursor.execute("select * from student")
# 获取查询结果
result: tuple = cursor.fetchall() # 游标对象使用fetchall()方法，得到的是全部的查询结果，是一个元组。这个元组内部嵌套了元组，嵌套的元组就是一行查询结果。
for r in result:
    print(r)
# 关闭连接
connection.close()