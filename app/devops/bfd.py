#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 除法总是会返回真实的商，不管操作数是整形还是浮点型。执行from future import division 指令就可以做到这一点。
from __future__ import division # 需要放到文件最开头
import os
import sys
import getopt


# https://blog.csdn.net/beautygao/article/details/79231571
'''
http://andylin02.iteye.com/blog/1071448
http://www.runoob.com/python/python-command-line-arguments.html
https://www.cnblogs.com/saiwa/articles/5253713.html
'''
# 声明全局变量
global total_size
# 给全局变量赋值
total_size = 0L


def get_dir_size(base_dir):
    base_dir = unicode(base_dir, 'utf-8')
    # 如果文件不存在，直接返回
    if not os.path.exists(base_dir):
        print("%s 不存在" % base_dir )
        return 0

    if os.path.isfile(base_dir):
        return os.path.getsize(base_dir)
    '''
    os.walk()是一个简单易用的文件、目录遍历器，可以帮助我们高效地处理文件、目录方面的问题。
    os.walk()函数的声明为：
    walk(top, topDown=True, onerror=None, followlinks=False)
    参数：
    top：所要遍历的目录的地址。
    topDown为真，则优先遍历top目录，否则优先遍历top的子目录，默认为：True。
    onerror：需要一个callable对象，当walk需要异常时，会调用。
    followlinks：如果为真，则会遍历目录下的快捷方式实际所指的目录，默认为：False

    os.walk 的返回值是一个生成器，也就是说我们需要不断地遍历它，来获得所有的内容。

    每次遍历的对象都返回的是一个三元组(root, dirs, files)
    root：所指的是当前正在遍历的这个目录本身的地址。
    dirs：一个list，当前目录下所有目录的名字，不包括子目录。
    files：一个list，当前目录下的所有文件的名字，不包括子目录中的文件。

    如果topDown参数为真，walk会遍历top目录，与top目录中的每一个子目录。
    '''
    # 再次声明，表示这里使用的是全局变量，而不是局部变量。
    total_size = 0L
    for root, dirs, files in os.walk(base_dir):
        # 处理root目录下的所有文件
        for xfile in files:
            total_size = total_size + os.path.getsize(os.path.join(root.encode('utf-8'), xfile.encode('utf-8')))

        # 处理root目录下的子目录
        for xdir in dirs:
            total_size = total_size + get_dir_size(os.path.join(root.encode('utf-8'), xdir.encode('utf-8')))

    return total_size


def readable(file_size):
    """

    :param file_size:
    :return:
    """
    k, m, g, t, p = 1024, 1024**2, 1024**3, 1024**4, 1024**5
    if file_size < k:
        return format(file_size, '.2f') + 'B'
    elif file_size < m:
        return format((file_size / k), '.2f') + 'KB'
    elif file_size < g:
        return format((file_size / m), '.2f') + 'MB'
    elif file_size < t:
        return format((file_size / g), '.2f') + 'GB'
    elif file_size < p:
        return format((file_size / t), '.2f') + 'TB'
    else:
        return format((file_size / p), '.2f') + 'PB'


def main(argv):
    # 指定查找目录，默认为当前目录。
    base_dir = os.getcwd()
    # 默认显示500M以上的文件和目录
    min_size = 500
    # 指定排序规则，默认为：asc，即升序。
    sort = 'asc'
    # 指定查找类型，默认为：all，即查找所有的文件和目录，可选项为：file，directory   -a -f -d
    xtype = 'all'
    # 指定查找层级，以base_dir为基础目录级计算，默认查找到最内层。
    level = 128

    try:
        opts, args = getopt.getopt(argv, 'dstSLh', ['--size=', '--type=', '--sort=', '--level=', '--help='])
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
        elif opt == '-d':
            base_dir = arg
        elif opt in ('-S', '--sort='):
            sort = arg
        elif opt in ('-s', '--size='):
            min_size = arg
        elif opt in ('-L', '--level='):
            level = arg
        else:
            print("非法参数")
            usage()


def usage():
    print('usage：python bfd.py [options] ')


def sort():
    print('指定排序方式，默认按升序排列')


def size():
    print('指定查找的大小，默认显示大小超过500M的文件或目录')


def xtype():
    print('指定查找的类型，文件或者目录')


def level():
    print('指定查找的层级')


if __name__ == '__main__':
    print(get_dir_size('C:\\Users\\Administrator\\Desktop\\中建项目'))
    print(readable(get_dir_size('C:\\Users\\Administrator\\Desktop\\中建项目')))

    print("Hello World")
    #main(sys.argv[1:])

