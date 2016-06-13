# _*_ coding:utf-8 _*_
from multiprocessing import Pool
import os
import time


def pro_do(process_num):
    print("Child process id is %d" % os.getpid())
    time.sleep(6 - process_num)
    print("This is process %d" % process_num)

if __name__ == "__main__":
    print("Current process is %d" % os.getpid())
    p = Pool()
    for i in range(5):
        p.apply_async(pro_do, (i,))
    p.close()
    p.join()
    print("Pool process done")
