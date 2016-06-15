# _*_ coding:utf-8 _*_
from multiprocessing import Process
import os


def pro_do(name, func):
    print(u'This is child process {0:d} from parent process {1:d}, and name is {2:s} which is used for {3:s}'.format(
        os.getpid(), os.getppid(), name, func))
if __name__ == "__main__":
    print(u'Parent process id {0:d}'.format(os.getpid()))
    pro = Process(target=pro_do, args=('test', 'dev'))
    print("Start child process")
    pro.start()
    pro.join()
    print("Process end")