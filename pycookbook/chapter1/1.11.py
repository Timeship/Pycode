#!/usr/bin/python
#-*- coding:utf-8 -*-

'''命令切片'''
record = '....................100 .......513.25 ..........'
cost = int(record[20:23])*float(record[31:37])
print(cost)

SHARES = slice(20,23)
PRICE = slice(31,37)
cost = int(record[SHARES])*float(record[PRICE])

'''slice函数创建了一个切片对象,a.stop,a.stop,a.step获取更多的属性'''
a = slice(5,50,2)
a.start
a.stop
a.step

'''通过调用切片的 indices(size) 方法将它映射到一个确定大小的序列上，
这个方法返回一个三元组 (start, stop, step) ，
所有值都会被合适的缩小以满足边界限制，
从而使用的时候避免出现 IndexError 异常'''

s = 'HelloWorld'
a.indices(len(s))
for i in range(*a.indices(len(s))):
    print(s[i])

for i in range(a.indices(len(s))):
    print(i)
