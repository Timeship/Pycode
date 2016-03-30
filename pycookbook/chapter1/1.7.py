#!/usr/bin/python
#-*- coding:utf-8 -*-

'''字典排序
   为了控制一个字典中的元素顺序
'''

from collections import OrderedDict
import json
def ordered_dict():
    d = OrderedDict()
    #d = defaultdict()
    d['foo'] = 1
    d['bar'] = 2
    d['spam'] = 3
    d['grok'] = 4
    for key in d:
        print(key,d[key])
    json.dumps(d)

if __name__=='__main__':
    ordered_dict()

'''
OrderedDict 内部维护着一个根据键插入顺序排序的双向链表。每次当一个新的元素插入进来的时候， 它会被放到链表的尾部。对于一个已经存在的键的重复赋值不会改变键的顺序。
一个OrderedDict的大小是普通字典的两倍
'''
