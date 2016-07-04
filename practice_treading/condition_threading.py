# _*_ coding:utf_8 _*_
''' Python 提供了 Condition对象。它除了具有acquire和release方法之外，还提供了wait和notify方法。线程首先acquire一个条件变量锁。如果条件不足，则该线程wait，如果满足就执行线程，甚至可以notify其他线程。其他处于wait状态的线程接到通知后会重新判断条件。
条件变量可以看成不同的线程先后acquire获得锁，如果不满足条件，可以理解为被扔到一个（Lock或Rlock）的waiting池。直达其他线程notify之后再重新判断条件。该模式常用语生产消费模式'''

import time
import threading
import random

queue = []

con = threading.Condition()


class Producer(threading.Thread):

    def run(self):
        while True:
            if con.acquire():
                if len(queue) > 100:
                    con.wait()
                else:
                    elem = random.randrange(100)
                    queue.append(elem)
                    print(
                        "Producer a elem {}, Now size is {}".format(elem, len(queue)))
                    time.sleep(random.random())
                    con.notify()
                con.release()


class Consumer(threading.Thread):
    def run(self):
        while True:
            if con.acquire():
                if len(queue) < 0:
                    con.wait()
            else:
                elem = queue.pop()
                print("Consumer a elem {}. Now size is {}".format(elem, len(queue)))
                time.sleep(random.random())
                con.notify()
            con.release()


def main():
    for i in range(3):
        Producer().start()

    for i in range(2):
        Consumer().start()
