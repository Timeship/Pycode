#!/usr/bin/python
#-*- coding:utf-8 -*-

'''通过某个字段将记录分组'''

rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]

'''先按照指定的字段,这里是date,排序，然后调用itertools.groupby()'''
from operator import itemgetter
from itertools import groupby

rows.sort(key=itemgetter('date'))

for date, items in groupby(rows,key=itemgetter('date')):
    print(date)
    for i in items:
        print(' ',i)

'''groupby() 函数扫描整个序列并且查找连续相同值(或者根据指定key函数返回值相同)的元素序列。
在每次迭代的时候，它会返回一个值和一个迭代器对象，
这个迭代器对象可以生成元素值全部等于上面那个值的组中所有对象。'''

'''必须要先排序，因为groupby()仅仅检查连续的元素'''

'''如果只分组，可以defaultdict'''
from collections import defaultdict
rows_by_date = defaultdict(list)
for row in rows:
    rows_by_date[row['date']].append(row)
