"""
面向对象：继承的基础语法
语法：
 class 类名(父类名):
    类内容体
注：继承分为单继承和多继承，将从父类哪里继承（复制）来成员变量和成员方法（不含私有）
"""

# 演示单继承
class Phone:
    prince = None # 价格
    producer = "Xiaomi" # 生产商

    def call_by_4g(self):
        print("4g通话")

class Phone2022(Phone):
    face_id = "1111" # 面部识别ID

    def call_by_5g(self):
        print("5g通话")

phone = Phone2022()
phone.prince = 10000
print(f"手机价格：{phone.prince}，手机生产商：{phone.producer}")
phone.call_by_4g()
phone.call_by_5g()
