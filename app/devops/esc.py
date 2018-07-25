#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import os
import datetime
import json
import sys
import getopt


# 清理过期es数据，做成命令行的方式

# elasticsearch 配置信息，以全局变量的方式配置
protocol = os.getenv('es_protocol') or 'http'
es_host = os.getenv('es_host') or '10.10.24.75'
es_http_port = os.getenv('es_http_port') or '9200'
es_tcp_port = os.getenv('es_tcp_port') or '9300'
es_user = os.getenv('es_user') or 'esadmin'
es_password = os.getenv('es_password') or 'esadmin'
es_url = protocol + '://' + es_host + ':' + es_http_port


def delete_index(index_name):
    '''
    删除elasticsearch索引
    :param index_name: 待删除的索引名称
    :return:
    '''
    request_url = es_url + '/' + index_name
    # 删除索引
    resp = requests.delete(request_url)
    # 解析JSON格式返回值，得知操作是否成功，以便进行下一步操作。result = json.loads(resp.content)['acknowledged']
    result_code = resp.status_code
    if result_code == 200:
        print("索引 %s 删除成功。" % index_name)
        return True
    elif result_code == 404:
        print('索引 %s 不存在。' % index_name)
        return False
    else:
        print('未知错误。')
        return False


def create_index(index_name):
    """
    创建elasticsearch索引
    :param index_name: 待创建的索引名称
    :return:
    """
    # 构造请求的 url
    request_url = es_url + '/' + index_name
    # 执行PUT请求，创建索引
    resp = requests.put(request_url)
    # 获取响应状态码
    result_code = resp.status_code
    if result_code == 200:
        print('创建索引 %s 成功' % index_name)
        return True
    elif result_code == 404:
        print('创建索引 %s 失败' % index_name)
        return False
    else:
        print('未知错误。')
        return False


def search_index(index_prefix):
    """
    获取以index_prefix开头的索引
    :param index_prefix: 索引前缀
    :return:
    """
    # 查找所有索引
    request_url = es_url + '/' + '_cat/indices'
    headers = {'Content-Type': 'application/json'}
    resp = requests.get(request_url, headers=headers)
    result_code = resp.status_code
    if result_code == 200:
        """
        得到一个List，每个元素为一个索引的信息
        从而，可以使用两种方式：
        1、循环遍历List，获得index的值并过滤。
        2、使用jsonpath，直接获取index的值并过滤，一个表达式即可解决。实际没走通
        """
        # 获取所有 index 的值并过滤出以 index_prefix 开头的索引
        rt = json.loads(resp.content)
        # 存储查询并过滤后的索引
        rt_list = []
        for item in rt:
            full_index_name = item['index']
            # 过滤出以 index_prefix 开头的索引
            if full_index_name.startswith(index_prefix):
                rt_list.append(full_index_name)

        return rt_list
    elif result_code == 404:
        print("当前Elasticsearch节点 %s:%s 未找到以 %s 为前缀的索引。" % (es_host, es_http_port, index_prefix))
        return None
    else:
        print('未知错误。')
        return None


def create_multi_index(index_prifix):
    """
    创建多个索引
    :param index_prifix:
    :return:
    """
    # 创建索引，构造测试数据
    for item in range(1, 6):
        index_date = (datetime.datetime.now() - datetime.timedelta(days=item)).strftime('%Y-%m-%d')
        full_index_name = index_prifix + '_' + index_date
        create_index(full_index_name)


def usage():
    print('usage: esc.py [options]                                        ')
    print('-i, --index: 指定待删除索引前缀或名称, 必须指定.                 ')
    print('-s, --separator: 指定索引与日期之间的分隔符, 默认为：-.          ')
    print('-f, --format: 指定日期格式, 默认为: %Y-%m-%d, 例如: 2018-07-22. ')
    print('-h, --help: 输出帮助信息.                                       ')


def test():
    # create_index("along")

    """
    for i in range(1, 6):
        index_date = (datetime.datetime.now() - datetime.timedelta(days=i)).strftime('%Y-%m-%d')
        delete_index('along' + '_' + index_date)
    """

    """
    index_list = search_index('along')
    for item in index_list:
        print(item)
    """


def main(argv):
    index = ''
    separator = '_'
    xformat = '%Y-%m-%d'
    # 读取参数
    try:
        opts, args = getopt.getopt(argv, 'i:sfh', ['--index=', '--separator', '--format', '--help'])
    except getopt.GetoptError:
        usage()
        sys.exit()
    # 获取详细参数
    for opt, arg in opts:
        if opt in ('-i', '--index='):
            index = opt
        elif opt in ('-s', '--separator='):
            separator = opt
        elif opt in ('-f', '--format='):
            xformat = opt
        elif opt in ('-h', '--help'):
            usage()
            sys.exit()
        else:
            print('未知的参数。')
            usage()
            sys.exit()

    # 执行命令
    if index:
        count = 1
        # 循环删除今天之前的所有索引
        while True:
            index_date = (datetime.datetime.now() - datetime.timedelta(days=count)).strftime(xformat)
            full_index_name = index + separator + index_date
            # 查询查询所有符合条件的索引
            index_list = search_index(full_index_name)
            # 删除查询出的所有索引
            if index_list:
                for item in index_list:
                    delete_index(item)
            count = count + 1
    else:
        print("必须指定索引前缀或索引名称。")
        usage()
        sys.exit()


if __name__ == '__main__':
    main(sys.argv[1:])
