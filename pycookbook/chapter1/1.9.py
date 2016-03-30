#!/usr/bin/python
#-*- coding:utf-8 -*-

'''查找两字典的相同点(相同的键或值)'''

a = {
    'x':1,
    'y':2,
    'z':3
}
b = {
    'w':10,
    'x':11,
    'y':2
}
print(a.keys() & b.keys())
print(a.keys() - b.keys())
print(a.items() & b.items())

'''这些操作可以用来过滤字典元素，假如想用字典来构造一个排除几个指定键的字典'''
c = {key:a[key] for key in a.keys() -{'z','w'}}
print(c)
