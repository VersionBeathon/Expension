# _*_ coding:utf-8 _*_
'''为了支持在同一线程中多次请求同一资源，python提供了可重入锁（Rlock）
Rlock内部维护着一个Lock和一个counter变量，counter记录了acquire的次数，从而使得资源可以被多次require。直到一个线程所有的acquire都被release，其他的线程才能获得资源'''

import time
import threading

mutex = threading.RLock()


class MyThread(threading.Thread):

    def run(self):
        if mutex.acquire(1):
            print("thread {} get mutex".format(self.name))
            time.sleep(1)
            mutex.acquire()
            mutex.release()
            mutex.release()


def main():
    print("start main threading")

    threads = [MyThread() for i in range(10)]
    for t in threads:
        t.start()
    print("End Main threading")
main()