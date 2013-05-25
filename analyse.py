#!/usr/bin/env python
#coding=utf-8
from __future__ import print_function
import re
import urllib
f = open("3rdlist.txt","r")
s = f.readlines()
d = {}
for t in s:
    t = t.split()
    d[t[2]] = [t[3],t[5],t[6]]
    #print(d[t[2]][2])
def gethtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    page.close()
    return html
def getrankji(html):
    reg = '<td width=.*?>(.*?)</td><td width=.*? align="center"><font color=green>(.*?)计</font></td>\s+<td width="150px">(.*?)</td>\s+<td width="150px" align="center"><font color=blue>(.*?)</font></td>\s+<td align="center" width=".*?">\s+<a href="contest_status.php\?cid=1057\&result=1&username=(.*?)" target="_parent">(.*?)</a></td>'
    ranklistji = re.compile(reg).findall(html)
    return ranklistji
def getrankfei(html):
    reg = '<td width=.*?>(.*?)</td><td width=.*? align="center"><font color=green>(.*?)非</font></td>\s+<td width="150px">(.*?)</td>\s+<td width="150px" align="center"><font color=blue>(.*?)</font></td>\s+<td align="center" width=".*?">\s+<a href="contest_status.php\?cid=1057\&result=1&username=(.*?)" target="_parent">(.*?)</a></td>'
    ranklistfei = re.compile(reg).findall(html)
    return ranklistfei
def getsolved(html):
    reg = '<a href="contest_status.php\?cid=1057&result=1&username=(.*?)" target="_parent">(.*?)</a></td>'
    solved = re.compile(reg).findall(html)
    return solved
gettml = gethtml('http://acm.sdut.edu.cn:180/sdutoj/contest_inner_ranklist.php?cid=1057')
solvedlist = getsolved(gettml)
print("\n\n|================================专业组========================================|\n\n")
list_ji = getrankji(gettml)
n1 = 1
for i in list_ji:
    print(i[0],d[i[0]][0],d[i[0]][1],d[i[0]][2],i[1],i[5],"第%d名"%n1,sep="\t")
    n1+=1
print("\n\n|================================非专业组======================================|\n\n")
list_fei = getrankfei(gettml)
n2 = 1
for x in list_fei:
    print (x[0],d[x[0]][0],d[x[0]][1],d[x[0]][2],x[1],x[5],"第%d名"%n2,sep="\t")
    n2+=1
