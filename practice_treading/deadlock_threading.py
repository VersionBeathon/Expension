# _*_ coding:utf-8 _*_
# 死锁：当两个线程以上都需要获取锁，获得锁后却要等待另外锁释放。
import time
import threading
mutex_a = threading.Lock()
mutex_b = threading.Lock()


class MyThread(threading.Thread):

    def task_a(self):
        if mutex_a.acquire():
            print("thread {} get mutex a".format(self.name))
            time.sleep(1)
            if mutex_b.acquire():
                print("thread {} get mutex b".format(self.name))
                mutex_b.release()
            mutex_a.release()

    def task_b(self):
        if mutex_b.acquire():
            print("thread {} get mutex a".format(self.name))
            time.sleep(1)
            if mutex_b.acquire():
                print("thread {} get mutex b".format(self.name))
                mutex_b.release()

    def run(self):
        self.task_a()
        self.task_b()


def main():
    print("start main threading")
    threads = [MyThread() for i in range(2)]
    for t in threads:
        t.start()
    print("End Main threading")
