# _*_ coding:utf-8 _*_
''' 创建线程后，线程的几个状态
New 创建
Runable 就绪。等待调度
Running 运行
Blocked 阻塞。阻塞可能在 Wait Locked Sleeping
Dead 消亡
'''
import time
import threading


class MyThread(threading.Thread):

    def run(self):
        for i in range(5):
            print('thread {}, @number: {}'.format(self.name, i))
            time.sleep(1)


def main():
    print("Start main threading")

    # 创建三个线程

    threads = [MyThread() for i in range(3)]
    
    # 启动三个线程
    
    for t in threads:
        t.start()    
    print("End main threading")


if __name__ is '__main__':
    main()
main()