# _*_ coding:utf-8 _*_
''' 如果在短时间“同事并行”读取修改内存的数据，很可能造成数据不同步，为了避免线程不同步造成数据不同步，可以对资源加锁。访问资源的线程需要获得锁，才能访问'''
import time
import threading

# 创建锁
count = 0
mutex = threading.Lock()

class MyThread(threading.Thread):
    def run(self):
        global count
        time.sleep(1)
        # 获取锁，修改资源
        if mutex.acquire():
            for i in range(100):
                count += 1
            print('thread {} add 1, count is {}'.format(self.name, count))
            # 释放锁
            mutex.release()


def main():
    print("Start main threading")
    for i in range(10):
        MyThread().start()
    print("End Main threading")

main()        