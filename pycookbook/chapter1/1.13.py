#!/usr/bin/python
#-*- coding:utf-8 -*-

'''通过关键字排序一个字典列表'''

'''通过使用operator模块的itemgetter函数,'''

rows = [
    {'fname':'Brian','lname':'Jones','uid':1003},
    {'fname':'David','lname':'Beazley','uid':1002},
    {'fname':'John','lname':'Cleese','uid':1001},
    {'fname':'Big','lname':'Jones','uid':'1004'}
]

from operator import itemgetter
rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))
print(rows_by_fname)
print(rows_by_uid)

'''
operator.itemgetter() 函数有一个被rows中的记录用来查找值的索引参数。
可以是一个字典键名称， 一个整形值或者任何能够传入一个对象的 __getitem__() 方法的值。
如果你传入多个索引参数给 itemgetter() ，它生成的 callable 对象会返回一个包含所有元素值的元组，
并且 sorted() 函数会根据这个元组中元素顺序去排序。
'''
'''itemgetter() 有时候也可以用 lambda 表达式代替'''
rows_by_name = sorted(rows,key = lambda r:r['fname'])
rows_by_ifname = sorted(rows,key = lambda r:(r['fname'],r['uid']))
