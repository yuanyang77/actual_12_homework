#!/usr/bin/env python
# -*- coding: utf-8 -*-
#抱歉基础较差，老师的作业我有点做不出来，简单弄了点监控apache日志IP的脚本，实现topIP 归属地 baidu了不少
import urllib2,urllib
import sys
import time
reload(sys)
sys.setdefaultencoding('utf-8')
from collections import Counter
import os
liwaiip = ['59.46.22.351','59.46.22.352']
# riqi = time.strftime("%Y_%m_%d", time.localtime())
# logname = ('/home/wangyw/access_log-%s.log' %(riqi))
logname = ('/home/wangyw/access_log.log')
ipcount = []
urlcount = []
for x in open(logname).readlines():
    ip = x.split(' ')[0]
    url = x.split(' ')[7]
    ipcount.append(ip)
    urlcount.append(url)
iplist = Counter(ipcount)
urllist = Counter(urlcount)
# print '======正在分析的日志======'
# for ip,count1 in iplist.most_common(5):
#     print '[+] 访问IP: %s ,访问次数: %d' % (ip,count1)
#
# for url,count2 in urllist.most_common(15):
#     print '[+] 访问URL: %s ,访问次数: %d' % (url,count2)
top1ip = iplist.most_common(5)[0][0]
url = "http://freeapi.ipip.net/{}".format(top1ip)
req = urllib2.Request(url)
res_data = urllib2.urlopen(req)
res = res_data.read().decode('utf-8')
# csres = res_data.read().decode('utf-8')[2:4]

if iplist.most_common(5)[0][0]not in liwaiip:
    print iplist.most_common(5)[0][0]
    print iplist.most_common(5)[0][1]
    print res[7:9]
    print urllist.most_common(5)[0][0]
