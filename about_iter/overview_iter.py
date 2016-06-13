# _*_ coding:utf-8 _*_
a = [1, 2, 3, 4, 5]
print(type(a))
a = iter(a)
print(type(a))
for i in dir(a):
    print(i)
print(a.__iter__())
print(a)
print(a is a.__iter__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())

