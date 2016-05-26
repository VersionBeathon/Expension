# _*_ coding:utf-8 _*_
# join(timeout)方法将会等待直到线程结束。这将阻塞正在调用的线程，直到被掉用join()方法的线程结束。
import time
import threading


class MyThread(threading.Thread):

    def run(self):
        for i in range(5):
            print('thread {}, @number: {}'.format(self.name, i))
            time.sleep(1)


def main():
    print("Start main threading")
    threads=[MyThread() for i in range(3)]

    for t in threads:
        t.start()

    # 一次让新创建的线程执行 join

    for t in threads:
        t.join()

    print("End Main threading")

main()
