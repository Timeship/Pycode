#!/usr/bin/python
#-*- coding:utf-8 -*-

'''过滤序列元素'''
mylist = [1,4,-5,10,-7,2,3,-1]
print([n for n in mylist if n>0])

'''
使用列表推导的一个潜在缺陷就是如果输入非常大的时候会产生一个非常大的结果集，占用大量内存。
如果你对内存比较敏感，那么你可以使用生成器表达式迭代产生过滤的元素。
'''

pos = (n for n in mylist if n>0)
for x in pos:
    print(x)

values = ['1','2','-3','-','4','N/A','5']
def is_int(val):
    try:
        int(val)
        return True
    except ValueError:
        return False
ivals = list(filter(is_int,values))
print(ivals)

mylist = [1,4,-5,10,-7,2,3,-1]
import math
print([math.sqrt(n) for n in mylist if n>0])

clip_neg = [n if n>0 else 0 for n in mylist]
print(clip_neg)
clip_pos = [n if n<0 else 0 for n in mylist]
print(clip_pos)

'''
itertools.compress()
它以一个iterable对象和一个相对应的Boolean选择器序列作为输入参数，然后输出iterable对象中对应选择器为True的元素
'''
addresses = [
        '5412 N CLARK',
        '5148 N CLARK',
        '5800 E 58TH',
        '2122 N CLARK'
        '5645 N RAVENSWOOD',
        '1060 W ADDISON',
        '4801 N BROADWAY',
        '1039 W GRANVILLE',

]
counts = [ 0, 3, 10, 4, 1, 7, 6, 1 ]

from itertools import compress
more5 = [n >5 for n in counts]
print(list(compress(addresses,more5)))
