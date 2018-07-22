#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import os
import time

# 清理过期es数据，做成命令行的方式

protocol = os.getenv('es_protocol') | 'http'
es_host =os.getenv('es_host') | '172.20.17.4'
es_http_port = os.getenv('es_http_port') | '9200'
es_tcp_port = os.getenv('es_tcp_port') | '9300'
es_user = os.getenv('es_user') | 'esadmin'
es_password = os.getenv('es_password') | 'password'
es_url = protocol + '://' + es_host + ":" + es_http_port

'''
[root@localhost ~]# curl -XDELETE http://172.20.17.4:9200/zipkin-2018-07-14       # zipkin-2018-07-14为索引名称
{
    "acknowledged":true
}
'''


def delete_index(index_name, separator, date_str):
    '''
    删除elasticsearch索引
    :param index_name:
    :param separator: 索引名称与日期之间的分隔符，可能是：-，_，.等
    :param date_str: 时间，以秒计算
    :return:
    '''
    # 构造索引名称
    index = index_name + separator + date_str
    # 构造 url
    request_url = es_url + '/' + index + '?' + 'pretty=true'
    # 删除索引
    resp_json = requests.delete(request_url)
    # 解析JSON格式返回值，得知操作是否成功，以便进行下一步操作。
    acknowledged = resp_json['acknowledged']
    if acknowledged == 'true':  # 可能为：true，false，unknown
        print("%s" % index + '删除成功。')
    else:
        print('%s' % index + '删除失败。')

    return acknowledged


if __name__ == '__main__':
    # 时间字符串的构造
    xdate = time.time()
    date_format = '%Y-%m-%d'
    xtime = time.strftime(date_format, time.localtime(xdate))

    delete_index('zipkin', '-', xtime)
