#!/usr/bin/python
#-*- coding:utf-8 -*-

'''序列中出现次数最多的元素'''

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]
from collections import Counter
word_counts = Counter(words)
top_three = word_counts.most_common(3)
print(top_three)

'''作为输入,Counter对象可以接受任意的hashable序列对象. 在底层实现上,
一个Counter对象就是一个字典,将元素映射到它出现的次数上
'''
morewords = ['why','are','you','not','looking','in','my','eyes']
for word in morewords:
    word_counts[word] +=1

print(word_counts['eyes'])

'''或者也可以用update方法'''
print(word_counts.update(morewords))

'''Counter另一个鲜为人知的特性是可以和数学运算操作相结合'''
a = Counter(words)
b = Counter(morewords)
c = a+b
d = a-b
