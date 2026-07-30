"""
字符串的多种定义方式
"""

# 单引号
a = '我是字符串'
print(a)
print(type(a))
# 双引号
b = "我是字符串"
print(b)
print(type(b))
# 三引号
c = """我是字符串"""
print(c)
print(type(c))

print("=========================")

str1 = "黑马程序员"
print(str1) # 黑马程序员

str2 = '"黑马程序员"'
print(str2) # "黑马程序员"

str3 = "'黑马程序员'"
print(str3) # '黑马程序员'

print("=========================")

"""
字符串拼接
"""
# “+”号
# 左右两个字符串
print("字符串"+"拼接")
# 字符串变量+字符串
name = "小明"
print("我是"+name)
# 字符串与非字符串变量
age = 20
# print("今年"+age+"岁") # TypeError: can only concatenate str (not "int") to str

print("=========================")

"""
字符串格式化
 - %表示占位
 - s表示将变量编程字符串放入占位的地方
 - %d将内容转换成整数，放入占位的地方
 - %f将内容转换成浮点数，放入占位的地方
"""
msg = "今年%s岁" % age
print(msg) # 今年20岁

# 多个变量占位

var1 = 1
var2 = 2
test = "%s+%s=%s" % (var1, var2,var1+var2)
print(test)

print("=========================")

"""
格式化的精度控制
可以使用“m.n”来控制数据的宽度和精度
 - m，控制宽度，要求是数字（很少使用），设置的宽度小于数字自身，不生效
 - .n，控制小数点精度，要求是数字，会进行小数的四舍五入
"""
name = "美团"
set_up_year = 2006
stock_price = 19.99
msg = "我是：%s，成立于：%s,股价是：%f" % (name, set_up_year, stock_price)
print(msg) #我是：美团，成立于：2006,股价是：19.990000


msg = "我是：%s，成立于：%s,股价是：%.2f" % (name, set_up_year, stock_price)
print(msg) # 我是：美团，成立于：2006,股价是：19.99

num1 = 11
msg = "%5s" % num1
print(msg) #   11，前面是空格，加上数字共五位

print("=========================")

"""
字符串格式优化
通过语法：f"内容{变量}"的格式来快速格式化
这种写法不做精度控制，也不理会类型，适用于快速格式化字符串
"""
name = "美团"
set_up_year = 2006
stock_price = 19.99
msg = f"我是：{name}，成立于：{set_up_year},股价是：{stock_price}"
print(msg)


print("=========================")

"""
对表达式进行格式化
表达式：一条具有明确执行结果的代码语句
"""

