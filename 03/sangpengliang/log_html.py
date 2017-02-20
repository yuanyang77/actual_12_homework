#encoding=utf-8

#读取文件
logfile = open('www_access_20140823.log','r')
html_dict = {}
for info in logfile.readlines():
    if info.split():
        ip = info.split()[0]
        code = info.split()[8]
        key =  (ip , code)
        html_dict[key] = html_dict.setdefault(key,0) +1
logfile.close()
#生成html文件
htmlfile = open('index.html','w')
htmlfile.write('''
<html>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<title>日志IP统计</title>
<body>
<table border=1>
<tr>
<td>num</td>
<td>ip</td>
<td>code</td>
<td>count</td>
</tr>

''')
htmlfile.close()
#排序前十
sort_dict = {}
sort_list = []
for info_dict in html_dict:
    sort_dict[html_dict[info_dict]] = info_dict
    sort_list.append(html_dict[info_dict])

count =  len(sort_list)
for i in range(0,count):
    for j in range(i+1,count):
        if sort_list[i] < sort_list[j]:
            temp = sort_list[i]
            sort_list[i] = sort_list[j]
            sort_list[j] = temp
sort_list = sort_list[0:10]
#追加信息到html文件中
htmlfile = open('index.html','a+')
i = 1
for info_key in sort_list:
    htmlfile.write('<tr><td>第 %d 名</td><td>%s</td><td>%s</td> <td>%s</td></tr> \n' %(i,sort_dict[info_key][0],sort_dict[info_key][1],info_key))
    i += 1
htmlfile.write('''
</body>
</html>
''')
htmlfile.close()




