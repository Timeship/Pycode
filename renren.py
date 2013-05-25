#!/usr/bin/env python
#coding=utf-8
import urllib
import urllib2
import cookielib
import re
from sgmllib import SGMLParser
from datetime import *
class Loginrenren(SGMLParser): 
    friendlist = [] 
    header = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:16.0) Gecko/20100101 Firefox/16.0'} 
    def __init__(self,username,password):
        SGMLParser.__init__(self)
        self.username = username
        self.password = password
        cj = cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        urllib2.install_opener(opener)
    def login(self):
        '''login in and return uid'''
        logpage = "http://www.renren.com/Login.do"
        data = {'email':self.username,'password':self.password}
        login_data = urllib.urlencode(data)
        res = urllib2.Request(logpage,login_data)
        self.file=urllib2.urlopen(res).read()
        idPos = self.file.index("'id':'")
        self.uid=self.file[idPos+6:idPos+15]
        tokPos=self.file.index("get_check:'")
        self.tok=self.file[tokPos+11:tokPos+21]
        rtkPos=self.file.index("get_check_x:'")
        self.rtk=self.file[rtkPos+13:rtkPos+21]
        #html = res.read()
        print 'login now...'
        print "Getting user id of you now"
        res = urllib2.urlopen("http://www.renren.com/home")
        html = res.read()
        uid = re.search("'ruid':'(\d+)'",html).group(1)
        print "login and got uid successfully"
        return uid
    def getfriendlist(self):
        req = urllib2.Request(url='http://friend.renren.com/myfriendlistx.do',headers = self.header)
        result = urllib2.urlopen(req).read()
        friend = str(re.search('friends=\[{.*}\]',result).group())
        friendId = re.findall(r'"id":(.*?),.*?,"name":"(.*?)"',friend)
        for f in friendId:
            self.friendlist.append(f)
            print f[1].decode('unicode-escape')
    def postmessage(self,content):
        url = "http://shell.renren.com/"+self.uid+"/status"
        postdata = {'content':content,
                    'hostid':self.uid,
                    'requetToken':self.tok,
                    '_rtk':self.rtk,
                    'channel':'renren',
                   }
        log_data = urllib.urlencode(postdata)
        req2 = urllib2.Request(url,log_data)
        self.hax = urllib2.urlopen(req2).read()
        print '在'+datetime.now().strftime('%Y-%m-%d %H:%M:%S %p')+' 你发送了一条为 "'+content+'" 的消息'
users = Loginrenren('youremailaddress',"yourpassword")
users.login()
users.getfriendlist()
content = raw_input("请输入内容:")
users.postmessage(content)
