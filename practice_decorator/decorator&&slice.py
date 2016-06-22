import time


def timeit(func):
    def wrapper():
        start = time.clock()
        func()
        stop = time.clock()
        print('Used time:', stop - start)
    return wrapper()


@timeit
def foo():
    print('such a decorator')
