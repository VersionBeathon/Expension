# _*_ coding:utf-8 _*_
'''线程可以读取共享的内存，通过内存做一些数据处理。这就是线程通信的一种，
python还提供了更加高级的线程通信接口。Event对象可以用来进行线程通信，调用event对象的wait方法，
线程组会阻塞等待，直到别的线程set之后，才会被唤醒。'''
import time
import threading


class MyThread(threading.Thread):

    def __init__(self, event):
        super(MyThread, self).__init__()
        self.event = event

    def fun(self):
        print("thread {} is ready".format(self.name))
        self.event.wait()
        print("thread {} run".format(self, name))

signal = threading.Event()

def main():
    start = time.time()
    for i in range(3):
        t = MyThread(signal)
        t.start()
    time.sleep(3)
    print("after {}s".format(time.time - start))
    signal.set()
