#!/usr/bin/python
#-*- coding:utf-8 -*-

'''转换并同时计算数据'''

'''一个非常优雅的方式去结合数据计算与转换就是使用一个生成器表达式参数。'''

nums = [1,2,3,4,5]
s = sum(x*x for x in nums)

import os
files = os.listdir()
if any(name.endswith('.py') for name in files):
    print('there be python')
else:
    print('sorry')
s = ('ACME',50,123.45)
print(','.join(str(x) for x in s))
portfolio = [
        {'name':'GOOG', 'shares': 50},
        {'name':'YHOO', 'shares': 75},
        {'name':'AOL', 'shares': 20},
        {'name':'SCOX', 'shares': 65}

]
min_shares = min(s['shares'] for s in portfolio)
