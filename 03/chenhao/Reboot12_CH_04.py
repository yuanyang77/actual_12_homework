#!/usr/local/bin/python
#encoding:utf-8
f = open(r'C:\Users\CHENHAO\Desktop\www_access_20140823.log','r')
lines = f.readlines()
dic={}
for line in lines:
    if line.split( ):
        if line.split( )[0] not in dic:
            dic[line.split( )[0]]={}
            dic[line.split( )[0]][line.split( )[8]]=1
        elif line.split( )[8] not in dic[line.split( )[0]]:
            dic[line.split()[0]][line.split()[8]]=1
        else:
            dic[line.split()[0]][line.split()[8]]=dic[line.split()[0]][line.split()[8]]+1
f.close()
txt='''
<table border='1'>
    <tr>
        <td>
            IP
        </td>
        <td>
            STATUS
        </td>
        <td>
            COUNT
        </td>
    </tr>'''

for ip in dic:
    for status in dic[ip]:
        txt=txt+'<tr><td>'+ip+'</td><td>'+status+'</td><td>'+str(dic[ip][status])+'</td></tr>'
txt=txt+'</table>'
print txt

f = open(r'C:\Users\CHENHAO\Desktop\test3.html','w')
f.write(txt)
f.close()