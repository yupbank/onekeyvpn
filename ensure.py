#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
ensure.py
Author: yupbank
Email:  yupbank@gmail.com

Created on
2013-09-30
'''
import sh
import os


OP_F = {
        "Linux": ubuntu_install
        }

def ubuntu_install(package):
    return sh.apt_get("install", package)

def install_package(package, sys_type):
    return OP_F.get(sys_type, lambda x:x)(package)


def main():
    print sh.uname()
    #print sh.ifconfig()

if __name__ == '__main__':
    main()
