getmysql.py

#!/usr/bin/python
# -*- coding: utf-8 -*-



def master(filename,hostname,logfiles,load):

    new_list = []
    new_list1 = []
    new_dic = {}
    new_dic1 = {}
    new_dicops = []
    new_load = []
    with open(logfiles) as master_file:
        for x in master_file:
            sfile = x.split('\n')[0]
            new_dicops.append(sfile)
    with open(load) as master_file:
        for x in master_file:
            load_sfile = x.split('\n')[0]
            new_load.append(load_sfile)
    with open(filename) as master_file:
        for Ip in master_file:
            new_list.append(Ip.split('\n')[0])
        for user in new_list:
            new_dic[user] =new_dic.get(user,0) + 1
        for rever in new_dic:
            new_dic1[new_dic[rever]]=rever
        for ip_list in new_dic1:
            new_list1.append(ip_list)
        new_list1 =sorted(new_list1,reverse=True)
        count = 0
        for x in new_list1:
            count = count + x
        Writehtml = open('index.html','a+')
        Writehtml.write('''<table align="center" bgcolor='FFEBCD' cellspacing="1" cellpadding="2"  border='6'>\n\t<tr>\n\t\t<td>%s</td>\n\t\t<td align='center' >活跃IP</td>\n\t\t<td>COUNT:%s</td>\n\t\t<td bgcolor='FFD2D2'> Log: %s</td>\n\t\t<td bgcolor='28FF28'> 负载: %s</td>\n\t</tr>''' % (hostname,count,new_dicops[0],new_load[0]))
        for x in range(len(new_list1)):
            if new_list1[x] in new_dic1:
               Writehtml.write("\n\t<tr>\n\t\t<td align='center'> %s</td>\n\t\t<td>%s</td>\n\t\t<td align='center'> %s</td>\n\t</tr>" % (x+1,new_dic1[new_list1[x]],new_list1[x]))
        Writehtml.write('''<p></p> ''')
        Writehtml.close()
Writehtml = open('index.html','a+')
Writehtml.write('''<meta  http-equiv="refresh" content="8" charset=utf-8">''')
Writehtml.close()

master('/ops/file/mysqlmaster','maste','/ops/file/mysqlmaster.mysqlmaster','/ops/file/mysqlmaster.load')
master('/ops/file/mysqlslave1','slave1','/ops/file/mysqlslave1.mysqlslave1','/ops/file/mysqlslave1.load')
master('/ops/file/mysqlslave3','slave3','/ops/file/mysqlslave3.mysqlslave3','/ops/file/mysqlslave3.load')
master('/ops/file/mysqlslave4','slave4','/ops/file/mysqlslave4.mysqlslave4','/ops/file/mysqlslave4.load')