# _*_ coding:utf-8 _*_
# Python 函数式编程的基本单元
from functools import reduce

# lambda

double_func = lambda s: s * 2

# map

print(map(double_func, [1, 2, 3, 4, 5]))
plus = lambda x, y: (x or 0) + (y or 0)
print(map(plus, [1, 2, 3], [4, 5, 6]))
print(map(plus, [1, 2, 3], [4, 5, 6, 7]))
print(map(None, [1, 2, 3, 4]))

# reduce

add = lambda x, y: x + y
print(reduce(add, [1, 2, 3, 4, 5]))
print(reduce(add, [1, 2, 3, 4, 5], 10))

# filter

mode2 = lambda x: x % 2
print(filter(mode2, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# 替换条件控制语句

''' 使用 布尔表达式中的 短路处理方式 
·f(x) and g(y)中，当f(x)为false时，不会再执行g(y)，直接返回false
·f(x) or g(y)中，当f(x)为true时，不会再执行g(y)，直接返回true
'''
pr = lambda s: s
print_num = lambda x: (x is 1 and pr("one")) or (
    x is 2 and pr("two")) or (pr("other"))
print(print_num(1))

''' print_num 等价于 
if x is 1 : pr("one")
elif x is 2 : pr("one")
or : pr("other")
'''

# 替换 for 循环

'''for e in lst: func(e) 
   map(func, lst)
'''

square = lambda x: x * x
for x in [1, 2, 3, 4, 5]:
    print(square(x))
print(map(square, [1, 2, 3, 4, 5]))

# 替换 while 循环

# 过程式：


def echo_IMP():
    while 1:
        x = input("IMP --")
        print(x)
        if x is 'quit':
            break
echo_IMP()

# 函数式：


def monadic_print(x):
    print(x)
    return(x)
ehco_FP = lambda: monadic_print(input("FP --")) is 'quit' or ehco_FP()

