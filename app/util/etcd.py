#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests, json

etcd_base_url = 'http://10.10.24.28:2379'


def get_etcd_version():
    current_uri = etcd_base_url + '/version'
    resp = requests.get(current_uri)
    # json.loads 用于解码JSON数据。该函数返回Python字段的数据类型。
    version_json = resp.json()
    return version_json['etcdserver']


def get_all_keys():
    current_uri = etcd_base_url + '/v2/keys'
    resp = requests.get(current_uri)
    return resp.json()


def get_value_from_key_path(key_path):
    current_url = etcd_base_url + key_path
    resp = requests.get(current_url)
    print(resp.json())


if __name__ == '__main__':
    get_all_keys()
