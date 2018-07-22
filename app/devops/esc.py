#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

# 清理过期es数据，做成命令行的方式

protocol = 'http'
elasticsearch_host = '172.20.17.4'
elasticsearch_http_port = '9200'
elasticsearch_tcp_port = '9300'


def delete_index(index_name, separator, date, date_format):
    # 构造索引名称
    index = index_name + separator
    # 构造 url
    current_url = 'http://' + elasticsearch_host + ":" + elasticsearch_http_port + "/_template?pretty"
    resp = requests.get(current_url)
    print(resp.json())


if __name__ == '__main__':
    delete_index()
