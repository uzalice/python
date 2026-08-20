"""
演示多继承
在多个父类中，如果有同名的成员，那么默认以继承顺序（从左到右为优先级）
"""
class Phone:
    prince = None # 价格
    producer = "Xiaomi" # 生产商

    def call_by_4g(self):
        print("4g通话")

class NFCReader:
    nfc_type = "第五代"
    producer = "HM"

    def read_card(self):
        print("NFC读卡")

    def write_card(self):
        print("NFC写卡")


class RemoteControl:
    rc_type = "红外遥控"

    def control(self):
        print("红外遥控开启了")


# 这里的pass是占位语句，用来保证函数（方法）或类定义的完整行，表示无内容，空的意思
class MyPhone(Phone, NFCReader, RemoteControl):
    pass


phone = MyPhone()
phone.call_by_4g()
phone.read_card()
phone.write_card()
phone.control()

print(phone.producer)