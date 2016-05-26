# _*_ coding:utf-8 _*_
def outer(some_func):
    def inner():
        print("before some_func")
        ret = some_func()
        return ret + 1
    return inner
def foo():
    return 1
decorated = outer(foo)
print(decorated())
foo = outer(foo)
print(foo)
