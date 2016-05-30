# _*_ coding:utf-8 _*_
a_string = "This is a global variable"


def foo():
    print(a_string)
foo()


def foo1():
    a_string = "test"
    print(locals())
foo1()
print(a_string)


def foo2(x, y=0):
    return x - y
print(foo2(3, 1))

# print(foo())

print(foo2(y=1, x=3))
print("=====Cut-off Line====\n")



def outer():
    x = 1
    def inner():
        print(x)
    inner()
outer()
print("=====Cut-off Line====\n")


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def apply(func, x, y):
    return func(x, y)
print(apply(add, 2, 1))
print(apply(sub, 2, 1))
print("=====Cut-off Line====\n")


def outer1():
    def inner1():
        print("Inside inner")
    return inner1
foo3 = outer1()
print(foo3)
foo3()
print("=====Cut-off Line====\n")


def outer2():
    x = 2
    def inner2():
        print(x)
    return inner2
foo4 = outer2()
foo4()
print(foo4.func_closure)
print("=====Cut-off Line====\n")


def outer3(x):
    def inner3():
        print(x)
    return inner3
print1 = outer3(3)
print2 = outer3(4)
print1()
print2()