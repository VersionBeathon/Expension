from multiprocessing import Process
from multiprocessing import Queue
import os
import time


def write_queue(q):
    for name in ['First_pig', 'Second_pig', 'Third_pig']:
        print("Put name %s to queue" % name)
        q.put(name)
        time.sleep(2)
    print("Write data finished")


def read_queue(q):
    print("Begin to read data")
    while True:
        name = q.get()
        print('Get name %s from queue' % name)

if __name__ == "__main__":
    q = Queue()
    pw = Process(target=write_queue, args=(q,))
    pr = Process(target=read_queue, args=(q,))

    pw.start()
    pr.start()
    pw.join()
    pr.terminate()
