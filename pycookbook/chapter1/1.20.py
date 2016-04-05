#!/usr/bin/python
#-*- coding:utf-8 -*-

'''合并多个字典或映射'''
from collections import ChainMap
a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }
c = ChainMap(a,b)

'''
可以使用大部分的字典操作，ChainMap在逻辑上将它们合并成一个字典.
ChainMap类只是在内部创建了一个容纳这些字典的列表,如果出现重复键第一次出现的映射值会被返回

### 对于字典中的更新和删除操作总是针对列表中的第一个字典
'''

'''
也有update方法可以替代
'''
a = {'x':1,'2':3}
b = {'y':2,'z':4}
merged = dict(b)
merged.update(a)
'''
 这样会创建一个完全不同的字典对象，同时如果对原字典做了更新，这种改变不会反应到心的合并字典中去.
'''
