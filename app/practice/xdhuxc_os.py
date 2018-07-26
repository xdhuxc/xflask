#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import time

# os.path模块主要用于文件的属性获取

# sys.argv 是命令行参数列表
# len(sys.argv) 是命令行参数个数
# sys.argv[0]表示脚本名称

# 获取当前脚本的全路径，以反斜杠分隔目录
print("当前脚本的全路径为：%s" % sys.argv[0])

# 获取当前工作目录路径
print("当前脚本所在目录为：%s" % os.getcwd())
# 获取当前工作目录路径
print("当前工作目录路径为：%s" % os.path.abspath('.'))
# 获取当前工作目录路径
print("当前工作目录路径为：%s" % os.path.abspath(os.curdir))
# 获取当前工作目录的父目录
print("当前工作目录的父目录路径为：%s" % os.path.abspath('..'))

str_path = 'C:\\Users\\wanghuan\\Desktop'
# 判断str_path是否存在
if os.path.exists(str_path):
    print("%s" % str_path + ' 存在。')
elif os.path.isfile(str_path):
    print("%s" % str_path + ' 是文件。')
elif os.path.isdir(str_path):
    print("%s" % str_path + '是目录。')
elif os.path.islink(str_path):
    print('%s' % str_path + '是符号链接文件。')
elif os.path.abspath(str_path):
    print('%s' % str_path + '是绝对路径。')
# 获取文件或目录的大小，如果是目录，返回0L，以字节为单位
str_path = 'C:\\Users\\wanghuan\\Desktop\\ingress.yaml'
print('%s 的大小为：%dB' % (str_path, os.path.getsize(str_path)))

# 返回文件或目录的最后存取时间
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getatime(str_path))))
# 返回文件或者目录的最后修改时间
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getmtime(str_path))))
# 返回文件或者目录的创建时间
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getctime(str_path))))

# 规范化路径
print(os.path.normpath(str_path))


try:
    sys.exit(0)
except:
    print('sys_die')
finally:
    print('sys_cleanup')

try:
    os._exit(0)
except:
    print('os_die')
print('os_exit')

"""
os._exit() 会直接将 python 程序终止，之后的所有代码都不会继续执行。
sys.exit() 会引发一个SystemExit异常，如果这个异常没有被捕获，那么python解释器将会退出。如果有捕获此异常的代码，那么这些代码还是会执行，捕获这个异常可以做一些额外的清理工作。0为正常退出，其他（1~127）为不正常退出。

一般情况下使用sys.exit()即可，一般在fork出来的子进程中使用os._exit()。

一般来说，os._exit()用于在线程中退出，sys.exit()用于在主线程中退出。
"""