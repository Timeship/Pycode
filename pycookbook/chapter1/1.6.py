'''
字典中的键映射多个值
'''
d = {
    'a' : [1,2,3],
    'b' : [4,5]
}
e = {
    'a' : {1,2,3},
    'b' : {4,5}
}
from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['b'].append(2)
d['c'].append(3)

d = defaultdict(set)
d['a'].add('1')
d['b'].add('2')
d['c'].add('3')

d = {}
d.setdefault('a',[]).append(1)
d.setdefault('a',[]).append(2)
d.setdefault('b',[]).append(3)
'''setdefault每次调用都要创建一个新的初始值的实例(例子程序中的空列表[])'''

d = {}
pairs = [('yellow',1),('green',2),('blue',3)]
for key, value in pairs:
    if key not in d:
        d[key] = []
        d[key].append(value)
print(d)

d = defaultdict(list)
for key,value in pairs:
    d[key].append(value)
