"""
和文件处理相关的类定义
"""

import json
from data_define import Record

class FileReader:

    # 定义抽象方法
    def read_data(self) -> list[Record]:
        # 读取文件的数据，读到的每一条数据都转换为Record对象，将它们封装到list内返回即可
        pass

class TextFileReader(FileReader):

    def __init__(self,path):
        # 文件路径
        self.path = path

    # 重写read_data方法
    def read_data(self) -> list[Record]:
        file = open(self.path,"r",encoding="utf-8")
        record_list: list[Record] = []

        for line in file.readlines():
            # 字符串.strip()/字符串.strip(字符串)：移除首尾空格和换行符或指定字符串
            line = line.strip()
            line_list = line.split(",")
            record =  Record(line_list[0],line_list[1],int(line_list[2]),line_list[3])
            record_list.append(record)

        file.close()
        return record_list

class JSONFileReader(FileReader):

    def __init__(self,path):
        # 文件路径
        self.path = path

    # 重写read_data方法
    def read_data(self) -> list[Record]:
        file = open(self.path,"r",encoding="utf-8")
        record_list: list[Record] = []

        for line in file.readlines():
            data_dict = json.loads(line)
            record = Record(data_dict["date"],data_dict["order_id"],int(data_dict["money"]),data_dict["province"])
            record_list.append(record)

        file.close()
        return record_list

if __name__ == '__main__':
    text_file_reader = TextFileReader("E:/dev/python/python_ai_base/chapter13/ComprehensiveCase/2011年1月销售数据.txt")
    json_file_reader = JSONFileReader("E:/dev/python/python_ai_base/chapter13/ComprehensiveCase/2011年2月销售数据JSON.txt")
    list1 = text_file_reader.read_data()
    list2 = json_file_reader.read_data()

    for l in list1:
        print(l)

    for l in list2:
        print(l)