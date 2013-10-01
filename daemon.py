#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
daemon.py
Author: yupbank
Email:  yupbank@gmail.com

Created on
2013-09-30
'''
import sys, os, time, atexit
from signal import SIGTERM

 
class Daemon(object):
    def __init__(self, pidfile, stdin='/dev/null', stdout='/dev/null', stderr='/dev/null', stdin_mode='r', stdout_mode='a+', stderr_mode='a+'):
        self.stdin = stdin
        self.stdout = stdout
        self.stderr = stderr
        self.pidfile = pidfile
        self.stdin_mode = stdin_mode
        self.stdout_mode = stdout_mode
        self.stderr_mode = stderr_mode

    def daemonize(self):
        try:
            pid = os.fork()
            if pid > 0:
                sys.exit(0)
        except OSError, e:
            sys.stderr.write('fork #1 failed: %d (%s) \n'%(e.errno, e.strerror))
            sys.exit(1)

        os.chdir("/")
        os.setsid()
        os.umask(0)

        try:
            pid = os.fork()
            if pid > 0:
                sys.exit(0)
        except OSError, e:
            sys.stderr.write('fork #1 failed: %d (%s) \n'%(e.errno, e.strerror))
            sys.exit(1)

        sys.stdout.flush()
        sys.stderr.flush()
        stdin = file(self.stdin, self.stdin_mode)
        stdout = file(self.stdout, self.stdout_mode)
        stderr = file(self.stderr, self.stderr_mode, 0)
        os.dup2(stdin.fileno(), sys.stdin.fileno())
        os.dup2(stdout.fileno(), sys.stdout.fileno())
        os.dup2(stderr.fileno(), sys.stderr.fileno())

        atexit.register(self.delpid)
        pid = str(os.getpid())
        file(self.pidfile, 'w+').write('%s\n'%pid)

    def delpid(self):
        os.remove(self.pidfile)

    
    def start(self):
        try:
            pid_file = file(self.pidfile, 'r')
            pid = int(pid_file.read().strip())
            pid_file.close()
        except IOError, e:
            pid = None

        if pid:
            message = 'pid file %s already exits. Daemon running already? \n'
            sys.stderr.write(message%self.pidfile)
            sys.exit(1)

        self.daemonize()
        self.run()

    def stop(self):
        try:
            pid_file = file(self.pidfile, 'r')
            pid = int(pid_file.read().strip())
            pid_file.close()
        except IOError, e:
            pid = None

        if not pid:
            message = 'pid file %s not exits. Daemon not running? \n'
            sys.stderr.write(message%self.pidfile)
            return

        try:
            while 1:
                os.kill(pid, SIGTERM)
                time.sleep(0.1)
        except OSError, e:
            err = str(e)
            if err.find('No such process') > 0:
                if os.path.exists(self.pidfile):
                    os.remove(self.pidfile)
            else:
                print err
                sys.exit(1)

    def restart(self):
        self.stop()
        self.start()

    def run(self):
        pass
                
        
