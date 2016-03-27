#!/usr/bin/env python
# coding=utf-8
'''在某个集合中查找最大或者最小的N个元素
在heapq模块中有两个函数--nlargest()和nsmallest()
'''
import heapq

nums = [1,8,2,23,7,-4,18,23,42,37,2]
print(heapq.nlargest(3,nums))
print(heapq.nsmallest(3,nums))

portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
print(cheap)
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
print(expensive)

'''在一个集合中查找最小或最大的N个元素，并且N小于集合元素数量，
那么这些函数提供了很好的性能。 因为在底层实现里面
首先会先将集合数据进行堆排序后放入一个列表
'''
nums = [1,8,2,23,7,-4,18,23,42,37,2]
heapq.heapify(nums)
print(nums)
#print(heapq.heappop(nums))

print(sorted(nums)[:3])
