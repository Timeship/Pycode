#!/usr/bin/env python
# coding=utf-8
from collections import deque

def search(lines,pattern,history=5):
    previous_lines = deque(maxlen=history)
    for li in lines:
        if pattern in li:
            yield li,previous_lines
        previous_lines.append(li)

if __name__=='__main__':
    with open('about.txt') as f:
        for line,prevlines in search(f,'python',5):
            for pline in prevlines:
                print(pline)
            print(line)
            print('-'*20)
