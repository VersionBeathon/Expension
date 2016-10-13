#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __Time__    : 16/10/12 17:42
# __Author__  : Kira
# __File__    : judge_point_exist_region.py

from collections import namedtuple
point = namedtuple('point', ['x', 'y'])

x = point(0.5, 0.5)
y = point(1, 4)
z = point(3, 2)

def judge(px, py):
    point = [[1,1], [3,1] ,[2,4], [4,4]]
    state = False
    for i in range(4):
        for j in range(i+1, len(point)):
            sx = point[i][0]
            sy = point[i][1]
            tx = point[j][0]
            ty = point[j][1]
            if (sx == px and py == sy) or (tx == px and py == ty):
                print('yes')
                break
            if (sy < py and ty >= py) or (sy >= py and ty < py):
                x = sx + (py - sy) * (tx - sx) / (ty - sy)
                if x==px:
                    print('yes')
                    break
                if x > px:
                    state = not state
    if state == True:
        print('yes')
    else:
        print('no')
judge(z.x, z.y)