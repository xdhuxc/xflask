#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import datetime

xdhuxc_time = "2018-07-19 11:11:30"
# 将其转换为时间数组
time_struct = time.strptime(xdhuxc_time, "%Y-%m-%d %H:%M:%S")
print("时间数组为：%s" % time_struct)

# 转换为时间戳
time_stamp = int(time.mktime(time_struct))  #
print("时间戳为：%s" % time_stamp)

# 将时间戳转换为指定格式日期
local_time = time.localtime(time_stamp) # 返回值为时间元组
print(local_time)
str_time = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
print("日期为：%s" % str_time)


# 格式切换

# 转换为时间数组，然后转换为其他格式
slash_format = time.strftime("%Y/%m/%d %H:%M:%S", time_struct)
dot_format = time.strftime("%Y.%m.%d %H:%M:%S", time_struct)
year_month_format = time.strftime("%Y.%m", time_struct)
print("/ 分隔的日期为：%s" % slash_format)
print(". 分隔的日期为：%s" % dot_format)
print("年月显示的日期：%s" % year_month_format)


# 获取当前时间并转换为指定的格式

# 获取当前时间时间戳
now_time = int(time.time())
time_struct = time.localtime(now_time)
print("当前时间的时间戳为：%s" % time_struct)

# 获得三天前的时间的方法
# 获得时间数组格式的日期
three_days_ago = (datetime.datetime.now() - datetime.timedelta(days=3)) # timedelta()函数的参数有：days，hours，seconds，microseconds。
# 转换为其他格式
str_time = three_days_ago.strftime("%Y-%m-%d %H:%M:%S")
print("三天前的日期为：%s" % str_time)

# 使用datetime模块来获取当前的日期和时间
xdhuxc = datetime.datetime.now()
print("当前的日期和时间是：%s" % xdhuxc)
print("ISO格式的日期和时间是：%s" % xdhuxc.isoformat())
print("当前的年份是：%s" % xdhuxc.year)
print("当前的月份是：%s" % xdhuxc.month)
print("当前的日期是：%s" % xdhuxc.day)
print("当前的小时是：%s" % xdhuxc.hour)
print("当前的分钟是：%s" % xdhuxc.minute)
print("当前的秒数是：%s" % xdhuxc.second)
print("yyyy/mm/dd格式是：%s/%s/%s" % (xdhuxc.year, xdhuxc.month, xdhuxc.day))

# https://www.cnblogs.com/pyxiaomangshe/p/7918850.html