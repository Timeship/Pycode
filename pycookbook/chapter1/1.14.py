#!/usr/bin/python
#-*- coding:utf-8 -*-

'''排序不支持原声比较的对象'''

class User:
    def __init__(self,user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)

def sort_notcompare():
    users = [User(23),User(3),User(99)]
    print(users)
    print(sorted(users,key = lambda u:u.user_id))

from operator import attrgetter
users = [User(23),User(3),User(99)]
sorted(users,key = attrgetter('user_id'))

'''attrgetter() 函数通常会运行的快点，并且还能同时允许多个字段进行比较。
这个跟 operator.itemgetter() 函数作用于字典类型很类似
'''
by_name = sorted(users,key = attrgetter('last_name','first_name'))
min(users,key = attrgetter('user_id'))
max(users,key = attrgetter('user_id'))
