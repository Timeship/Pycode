#!/usr/bin/env python
#coding=utf-8
import MySQLdb
fp = open("/Pycode/xxx.txt")
conn = MySQLdb.connect('localhost','name','password','basename',charset ='utf8')
cur = conn.cursor()
for line in fp.readlines():
    cun = line.split()
    sql_content = "update contest_user set name1='%s',password = '%s' where id = %d;"%(cun[1],cun[4],int(cun[0])) 
    print sql_content
    cur.execute(sql_content)
    conn.commit()
