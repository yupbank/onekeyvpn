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
import sys


def ubuntu_install(package):
    return os.popen('sudo apt-get install %s -y'%package)

OP_F = {
        "Linux": ubuntu_install
        }

OP_PACKAGE = {
        "Linux": ['openswan', 'xl2tpd']
	}

def install_package(package, sys_type):
    return OP_F[sys_type](package)


def main():
    os_type = sh.uname().strip()
    for p in OP_PACKAGE[os_type]:
        for info in install_package(p, os_type):
            #sys.stdout.flush()
	        print info
    #print sh.ifconfig()

if __name__ == '__main__':
    main()
