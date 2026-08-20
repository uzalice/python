"""
SQL 综合案例，读取文件，写入MySQL数据库中
"""
from file_define import TextFileReader,JSONFileReader
from data_define import Record
from pymysql import Connection

text_file_reader = TextFileReader("E:/dev/python/python_ai_base/chapter13/ComprehensiveCase/2011年1月销售数据.txt")
json_file_reader = JSONFileReader("E:/dev/python/python_ai_base/chapter13/ComprehensiveCase/2011年2月销售数据JSON.txt")
january_data = text_file_reader.read_data()
february_data = json_file_reader.read_data()
# 一月和二月的数据合并
all_data : list[Record] = january_data + february_data

connection = Connection(
    host="localhost",
    user="root",
    password="itheima",
    autocommit=True
)

# 获取游标对象
cursor = connection.cursor()
# 选择数据库
connection.select_db("py_sql")
# 执行sql语句
for record in all_data:
    sql = f"insert into orders(order_date, order_id, money, province) "\
           f"values('{record.date}','{record.order_id}',{record.money},'{record.province}')"
    cursor.execute(sql)

connection.close()

