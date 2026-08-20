"""
复写和使用父类成员
就是Java中的复用，这里调用父类成员和方法可以使用super().xxx也可使用父类名.xxx，这里的父类名在形参中。
注意：一旦复写父类成员，那么类对象调用成员的时候就会调用复写后的新成员，如果需要使用被复写的父类的成员，需要特殊的调用方式
"""
class Phone:
    IMEI = None             # 序列号
    producer = "Xiaomi"     # 厂商

    def call_by_5g(self):
        print("使用5g网络进行通话")


# 定义子类，复写父类成员
class MyPhone(Phone):
    producer = "HuaWei"        # 复写父类的成员属性

    def call_by_5g(self):
        print("开启CPU单核模式，确保通话的时候省电")
        # 方式1
        # print(f"父类的厂商是：{Phone.producer}")
        # Phone.call_by_5g(self)
        # 方式2
        print(f"父类的厂商是：{super().producer}")
        super().call_by_5g()
        print("关闭CPU单核模式，确保性能")

phone = MyPhone()
print(f"phone`producer：{phone.producer}")
phone.call_by_5g()