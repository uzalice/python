"""
换行符号：\n
"""
name = "字节跳动"
stock_price = 19.99
stock_code = "003032"
stock_price_daily_growth_factor = 1.2
growth_days = 7
msg = (f"公司：{name}，股票代码：{stock_code}，当前股价：{stock_price}\n每日增长系数：{stock_price_daily_growth_factor}，"
       f"经过{growth_days}天的增长后，股价达到了：%.2f") % (stock_price * stock_price_daily_growth_factor ** growth_days)
print(msg)
