#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import jsonpath_rw
import jsonpath

"""
json.dumps()：用于将 Python 对象编码成 JSON 字符串
json.loads()：将已经编码的 JSON 字符串解析为 Python 对象。

Python 原始类型向 JSON 类型的转换对照表：
Python               JSON
dict                 object
list, tuple          array
string, unicode      string
int, long, float     number
True                 true
False                false
None                 null

JSON 类型转换到 Python 的类型对照表
JSON                 Python
object               dict
array                list
string               unicode
number(int)          int, long
number(real)         float
true                 True
false                False
null                 None
"""

original_str = """
[{"health":"yellow","status":"open","index":"xdhuxc-app_2018-07-20","pri":"5","rep":"1","docs.count":"0","docs.deleted":"0","store.size":"795b","pri.store.size":"795b"},{"health":"yellow","status":"open","index":"xdhuxc-app_2018-07-19","pri":"5","rep":"1","docs.count":"0","docs.deleted":"0","store.size":"795b","pri.store.size":"795b"}]
"""
python_list = []
# 将 JSON 格式的字符串转换为 Python List对象，List的元素为字典对象。
rt = json.loads(original_str)
# rt = [item["index"] for item in rt if item["index"].startswith('xdhuxc-app')]
for item in rt:
    print(item['index'])
    index_name = item['index']
    if index_name.startswith('xdhuxc-app'):
        python_list.append(item['index'])

# 获取
for item in python_list:
    print(item)

# 将 original_str 转换为 JSON 格式
json_format = json.dumps(original_str)
print(json_format)

# 获取 index
all_indexes = jsonpath.jsonpath(original_str, '$.')