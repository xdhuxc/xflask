#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fabric.api import run
from fabric.api import env
from fabric.api import local
from fabric.api import parallel

"""
1、生成 ssh-keygen
2、复制 ssh key 到各机器上
"""


def auto_ssh_copy_id(target_host, username, password):
    env.host_string = target_host
    env.user = username
    env.password = password

    print("")


def main():
    print("")