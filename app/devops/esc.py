#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import os
import time
import datetime

# 清理过期es数据，做成命令行的方式

# elasticsearch 配置信息，以全局变量的方式配置
protocol = os.getenv('es_protocol') or 'http'
es_host = os.getenv('es_host') or '10.10.24.75'
es_http_port = os.getenv('es_http_port') or '9200'
es_tcp_port = os.getenv('es_tcp_port') or '9300'
es_user = os.getenv('es_user') or 'esadmin'
es_password = os.getenv('es_password') or 'esadmin'
es_url = protocol + '://' + es_host + ':' + es_http_port
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
    request_url = es_url + '/' + index_name + '?' + 'pretty'
    print(request_url)
    # 删除索引
    resp = requests.delete(request_url)
    # 解析JSON格式返回值，得知操作是否成功，以便进行下一步操作。
    acknowledged = resp.json()['acknowledged']
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
        print(request_url)
        resp_json = requests.put(request_url)
        resp_json = resp_json.json()
        print(resp_json)
        #result = resp_json['acknowledged']
        if resp_json == 'true':
            print('创建索引 %s 成功' % full_index_name)
        else:
            print('创建索引 %s 失败' % full_index_name)


if __name__ == '__main__':
    #create_index("xdhuxc-app")
    for i in range(1, 6):
        index_date = (datetime.datetime.now() - datetime.timedelta(days=i)).strftime('%Y-%m-%d')
        delete_index('xdhuxc-app' + '_' + '2018-07-21')