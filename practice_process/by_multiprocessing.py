# _*_ coding:utf-8 _*_
from multiprocessing import Process
import os


def pro_do(name, func):
    print("This is child process %d from parent process %d, and name is %s which is used for %s" % (os.getpid(), os.getppid(), name, func))
if __name__ == "__main__":
    print("Parent process id %d" % os.getpid())
    pro = Process(target=pro_do, args=('test', 'dev'))
    print("Start child process")
    pro.start()
    pro.join()
    print("Process end")