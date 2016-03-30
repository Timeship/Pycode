#!/usr/bin/python
#-*- coding:utf-8 -*-

'''删除序列相同的元素并保持顺序'''

#如果序列都是hashable类型
def dedque(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

a = [1,5,2,1,9,1,5,10]
print(list(dedque(a)))

#非hashable的时候,不可哈希的时候，比如dict
def dedque(items,key = None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)

a = [{'x':1,'y':2},{'x':1,'y':3},{'x':1,'y':2},{'x':2,'y':4}]
list(dedque(a,key=lambda d:(d['x'],d['y'])))
