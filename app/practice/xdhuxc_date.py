#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

xdhuxc_time = "2018-07-19 11:11:30"
# 将其转换为时间数组
time_struct = time.strptime(xdhuxc_time, "%Y-%m-%d %H:%M:%S")
print("时间数组为：%s" % time_struct)

# 转换为时间戳
time_stamp = int(time.mktime(time_struct))  #
print("时间戳为：%s" % time_stamp)

# 将时间戳转换为指定格式日期
local_time = time.localtime(time_stamp)
str_time = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
print("日期为：%s" % str_time)

# https://www.cnblogs.com/pyxiaomangshe/p/7918850.html