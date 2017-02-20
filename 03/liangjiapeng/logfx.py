#!/bin/env python
#coding:utf8

#coding=utf8


#数据导入，写入到字典中

Sdict={}
Sdata=open('www_access.log','a+')
for i in Sdata:
    IP = i.split()[0]
    STAT = i.split()[8]
    Sdict.setdefault(IP+":"+STAT,0)
    Sdict[IP+":"+STAT] += 1
Sdata.close()


#分析数据，统计访问量最高的IP

Tmpdict={}
for y,z in Sdict.items():
    Tmpdict.setdefault(z,[])
    if z in Tmpdict:
        Tmpdict[z].append(y)
alist=Tmpdict.keys()
alist.sort()
alist.reverse()


#输出HTML格式
loguot=""
Ddata=open('index.html','w')
for i in range(10):
    counts=alist[i]
    ip=Tmpdict[alist[i]][0].split(":")[0]
    status=Tmpdict[alist[i]][0].split(":")[1]
    loguot = loguot +  "<tr><td> %s </td><td> %s </td><td> %s </td></tr>\n" %(ip,status,counts)
text="""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>日志分析</title>
</head>
<body>
<table cellspacing="0" cellpadding="2" bordercolor="#000000" border="1">
<tr><td> IP </td><td> STATUS </td><td> COUNT </td></tr>
%s
</table>
</body>
</html>
"""%loguot

Ddata.write(text)


Ddata.close()
