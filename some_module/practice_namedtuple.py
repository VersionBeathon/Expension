# _*_ coding:utf-8 _*_

# 创建坐标点:namedtuple

from collections import namedtuple
from collections import Counter
point = namedtuple('point', ['x', 'y'])
p = point(1, 2)
print(p.x)
print(p.y)
circle = namedtuple('Circle', ['x', 'y', 'r'])
c = circle(1, 1, 1)
print(c.x)
print(c.y)
print(c.r)

# Counter是一个简单的计数器,统计字符出现的个数:

c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
print(c)