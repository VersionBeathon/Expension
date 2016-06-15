# _*_ coding:utf-8 _*_
import time
from multiprocessing import Pool


def squareX(x):
    time.sleep(1)
    return x**2


if __name__ == "__main__":
    list_x = [1, 2, 3, 4, 5, 6]
    print('No process:')
    st = time.time()
    for x in list_x:
        squareX(x)
    ed = time.time()
    print('Run time:', int(ed - st))

    print('By process:')
    pool = Pool(5)
    result = pool.map(squareX, list_x)
    pool.close()
    pool.join()
    ed2 = time.time()
    print('Run time:', int(ed2 - ed))
    print(result)

