# _*_ coding:utf-8 _*_
def one(*args):
    print(args)


one(1, 2, 3)

one_get = lambda *args: args
print(one_get(1, 2, 3))


def two(x, y, *args):
    print(x, y, args)


two(1, 2, 1, 2)

two_get = lambda *args: args
print(two_get(1, 2, 3, 4, 5))


def add(x, y):
    return x + y


lst = [1, 2]
print(add(lst[0], lst[1]))
print(add(*lst))

add_get = lambda x, y: x + y
print(add_get(*lst))


# **代表字典的键值对


def foo(**kwargs):
    print(kwargs)


foo()
foo(x=1, y=2)

foo_get = lambda **kwargs: kwargs
print(foo_get(x=1, y=2))

dct = {'x': 1, 'y': 2}


def bar(x, y):
    return x + y


print(bar(**dct))

bar_get = lambda x, y: x + y
print(bar_get(**dct))


def loger(func):
    def inner(*args, **kwargs):
        print("Arguments were: %s, %s" % (args, kwargs))
        return func(*args, **kwargs)

    return inner


@loger
def foo1(x, y=1):
    return x * y


@loger
def foo2():
    return 2


foo1(5, 4)
foo2()
