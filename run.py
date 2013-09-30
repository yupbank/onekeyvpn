#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
run.py
Author: yupbank
Email:  yupbank@gmail.com

Created on
2013-09-30
'''
import sys
import os
import time
from daemon import Daemon
import SimpleHTTPServer
import BaseHTTPServer
from BaseHTTPServer import HTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler


PORT = 8000

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler


ROUTES = [
            ('/', '.')
            ]

class MyHandler( BaseHTTPServer.BaseHTTPRequestHandler):
    def do_POST(self):
        pass
    def translate_path(self, path):
        # default root -> cwd        
        root = os.getcwd()
        
        # look up routes and get root directory
        for patt, rootDir in ROUTES:
            if path.startswith(patt):                
                path = path[len(patt):]
                root = rootDir
                break
        # new path
        return os.path.join(root, path)

    def do_GET(self):
        return 'hah'

httpd = HTTPServer(('127.0.0.1', 8000), MyHandler)
class MyDaemon(Daemon):
    def run(self):
        print "serving at port", PORT
        httpd.serve_forever()


def main():
    da = MyDaemon('/Users/yupbank/projects/onekey_vpn/ha', stdout='/Users/yupbank/projects/onekey_vpn/t')
    da.start()



if __name__ == '__main__':
    httpd.serve_forever()
    #main()
