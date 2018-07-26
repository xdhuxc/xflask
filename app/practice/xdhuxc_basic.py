#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

# 含前不含后，，默认步长为：1
for i in range(1, 5):
    print(i)

base_dir = 'C:\\Users\\Administrator\\Desktop\\yztc'



global total_size
base_dir = unicode(base_dir)
for item in os.listdir(base_dir):
    print(base_dir)
    if os.path.isfile(item):
        print()
        full_path = os.path.join(base_dir, item)
        total_size = total_size + os.path.getsize(full_path)
    if os.path.isdir(item):
        total_size = total_size
    print(item)

"""
在 Python 中，False, 0, '', [], {}, ()都可以视为假。
"""