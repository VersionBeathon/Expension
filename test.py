import time

li = [lambda:x for x in range(10)]
print(li[0]())
print(li[2]())


def time_machine(func):

    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        print(u'共耗时:%s秒' % (time.time()-start_time))
    return wrapper()

@time_machine
def foo():
    time.sleep(3)





