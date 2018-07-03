#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests, json

etcd_base_url = 'http://10.10.24.28:2379'


def get_etcd_version():
    current_url = etcd_base_url + '/version'
    resp = requests.get(current_url)
    print(resp.json())


if __name__ == '__main__':
    get_etcd_version()
