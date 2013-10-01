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
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")



application = tornado.web.Application([
    (r"/", MainHandler),
])
PORT = 8000








class MyDaemon(Daemon):
    def run(self):
        print "serving at port", PORT
        sys.stdout.flush()
        application.listen(PORT)
        tornado.ioloop.IOLoop.instance().start()


def main():
    t = os.path.dirname(os.path.abspath(__file__))
    print t
    da = MyDaemon('%s/pid'%t, stdout='%s/log'%t, stdout_mode='w')
    print 'start'
    da.start()



if __name__ == '__main__':
    #tornado.ioloop.IOLoop.instance().start()
    main()
