#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

# 含前不含后，，默认步长为：1
for i in range(1, 5):
    print(i)

base_dir = 'C:\\Users\\Administrator\\Desktop\\yztc'
total_size = 0L


def get_dir_size(base_dir):
    global total_size
    base_dir = unicode(base_dir)
    for item in os.listdir(base_dir):
        if os.path.isfile(item):
            full_path = os.path.join(base_dir, item)
            print(full_path)
            total_size = total_size + os.path.getsize(full_path)
        if os.path.isdir(item):
            full_path = os.path.join(base_dir, item)
            print(full_path)
            total_size = total_size + get_dir_size(full_path)
    return total_size

print(get_dir_size(base_dir))

"""
在 Python 中，False, 0, '', [], {}, ()都可以视为假。
"""