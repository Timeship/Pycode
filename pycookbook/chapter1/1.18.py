#!/usr/bin/python
#-*- coding:utf-8 -*-

'''映射名称到序列元素'''

'''
collections.namedtuple()函数通过使用一个普通的元组对象来解决这个问题.
这个函数实际上是一个返回python中标准元组类型子类的一个工厂方法
'''
from collctions import namedtuple
Subscriber = namedtuple('Subscriber',['addr','joined'])
sub = Subscriber('john@example.com','2012-3-5')
print(sub)

'''
namedtuple 的实例看起来像一个普通的类实例，
但是它跟元组类型是可交换的，支持所有的普通元组操作，比如索引和解压。
'''
len(sub)
addr,joined = sub

'''
命名元组另一个用途就是作为字典的替代，因为字典存储需要更多的内存空间。
如果你需要构建一个非常大的包含字典的数据结构，那么使用命名元组会更加高效。
但是需要注意的是，不像字典那样，一个命名元组是不可更改的。
'''

'''
如果你真的需要改变然后的属性，那么可以使用命名元组实例的 _replace() 方法，
它会创建一个全新的命名元组并将对应的字段用新的值取代。
'''

'''
_replace() 方法还有一个很有用的特性就是当你的命名元组拥有可选或者缺失字段时候， 它是一个非常方便的填充数据的方法。
你可以先创建一个包含缺省值的原型元组，然后使用 _replace() 方法创建新的值被更新过的实例
'''
from collections import namedtuple
Stock = namedtuple('Stock',['name','shares','price','date','time'])
stock_prototype = Stock('',0,0,None,None)

def dict_to_stock(s):
    return stock_prototype._replace(**s)
