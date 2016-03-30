#!/usr/bin/python
#-*- coding:utf-8 -*-

'''字典的运算'''

prices = {
    'AMCE':45.23,
    'AAPL':612.78,
    'IBM':205.55,
    'HPQ':37.20,
    'FB':10.75
}

min_prices = min(zip(prices.values(),prices.keys()))
print(min_prices)
max_prices = max(zip(prices.values(),prices.keys()))
print(max_prices)

prices_sorted = sorted(zip(prices.values(),prices.keys()))

'''zip()函数创建的是一个只能访问一次的迭代器.下面的代码会产生错误'''
prices_and_names = zip(prices.values(),prices.keys())
print(min(prices_and_names))
#print(max(prices_and_names))

min(prices, key = lambda k :prices[k])
max(prices, key = lambda k :prices[k])

min_value = prices[min(prices,key = lambda k:prices[k])]
'''zip函数通过将字典反转为元组序列解决了上述问题,当比较两个元组的时候,值会先进行比较,然后是键'''


