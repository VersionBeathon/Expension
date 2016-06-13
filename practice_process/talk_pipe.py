# _*_ coding:utf-8 _*_
from multiprocessing import Process
from multiprocessing import Pipe
import os
import time
import sys


def send_pipe(p):
    names = ['First_pig', 'Second_pig', 'Third_pig']
    for name in names:
        print('Put name %s to pipe' % name)
        p.send(name)
        time.sleep(1)


def recv_pipe(p):
    print("Try to read data in pipe")
    while True:
        name = p.recv()
        print("Get name %s from pipe" % name)

if __name__ == "__main__":
    ps_pipe, pr_pipe = Pipe()
    ps = Process(target=send_pipe, args=(ps_pipe,))
    pr = Process(target=recv_pipe, args=(pr_pipe))
    pr.start()
    ps.start()
    ps.join()
    pr.terminate()
