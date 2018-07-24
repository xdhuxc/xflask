#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import os
import time
import datetime

# 清理过期es数据，做成命令行的方式

# elasticsearch 配置信息，以全局变量的方式配置
protocol = os.getenv('es_protocol') | 'http'
es_host =os.getenv('es_host') | '172.20.17.4'
es_http_port = os.getenv('es_http_port') | '9200'
es_tcp_port = os.getenv('es_tcp_port') | '9300'
es_user = os.getenv('es_user') | 'esadmin'
es_password = os.getenv('es_password') | 'password'
# 构造 elasticsearch URL 例如，http://192.168.91.128:9200
es_url = protocol + '://' + es_host + ":" + es_http_port

'''
[root@localhost ~]# curl -XDELETE http://172.20.17.4:9200/zipkin-2018-07-14       # zipkin-2018-07-14为索引名称
{
    "acknowledged":true
}
'''


def delete_index(index_name):
    '''
    删除elasticsearch索引
    :param index_name: 待删除的索引名称
    :return:
    '''
    # 构造 url
    request_url = es_url + '/' + index_name + '?' + 'pretty=true'
    # 删除索引
    resp_json = requests.delete(request_url)
    # 解析JSON格式返回值，得知操作是否成功，以便进行下一步操作。
    acknowledged = resp_json['acknowledged']
    if acknowledged == 'true':  # 可能为：true，false，unknown
        print("%s" % index_name + '删除成功。')
    else:
        print('%s' % index_name + '删除失败。')

    return acknowledged


def create_index(index_name):
    """
    构造测试数据
    :return:
    """
    # 创建索引，构造测试数据
    for i in range(1, 6):
        index_date = (datetime.datetime.now() - datetime.timedelta(days=i)).strftime('%Y-%m-%d')
        full_index_name = index_name + '_' + index_date
        request_url = es_url + '/' + full_index_name
        resp_json = requests.put(request_url)
        result = resp_json['acknowledged']
        if result == 'true':
            print('创建索引 %s 成功' % full_index_name)
        else:
            print('创建索引 %s 失败' % full_index_name)


if __name__ == '__main__':
    # 时间字符串的构造
    xdate = time.time()
    date_format = '%Y-%m-%d'
    xtime = time.strftime(date_format, time.localtime(xdate))
    """
    :param
    separator: 索引名称与日期之间的分隔符，可能是：-，_，.等
    :param
    date_str: 时间，以秒计算
    """
    full_index_name = 'zipkin' + '-' + xtime
    delete_index(full_index_name)
