#/usr/bin/env python
# _*_ coding:utf-8 _*_
# 作业
# 一个access_log（直接发群里），按照ip和访问状态两个维度统计数据，打印前十名，并且以html表格的形式展现
# 每一行大概是这样
# 61.159.140.123 - - [23/Aug/2014:00:01:42 +0800] "GET /favicon.ico HTTP/1.1" 404 \ "-" "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.66 Safari/537.36 LBBROWSER" "-"

# 提示

# s = '61.159.140.123 - - [23/Aug/2014:00:01:42 +0800] "GET /favicon.ico HTTP/1.1" 404 \ "-" "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.66 Safari/537.36 LBBROWSER" "-"'
# print s.split()[0] +'  ' + s.split()[8]

#第一步:读取日志文件

logfile = open('www_access_20140823.log','r')
res_dict = {}
for line in logfile.readlines():
    #print line.split()[0],line.split()[8]
    dict_key = (line.split()[0],line.split()[8])
    res_dict[(dict_key)] = res_dict.setdefault(dict_key,0) + 1
logfile.close()
#print res_dict

#第二步：排序
sort_dict ={}
sort_list = []
for dict_key in res_dict:
    #print dict_key
    #print res_dict[dict_key]
    sort_dict[res_dict[dict_key]] = dict_key
    #print res_dict[dict_key]
    sort_list.append(res_dict[dict_key])
#print sort_list
#print sort_dict
#冒泡排序

count = len(sort_list)
for i in range(0,count):
    for j in range(i+1,count):
        if sort_list[i] < sort_list[j]:
            swap = sort_list[i]
            sort_list[i] = sort_list[j]
            sort_list[j] = swap
            #arr[i],arr[j] = arr[j],arr[i]
#print sort_list

#截取前10个数据
sort_list = sort_list[0:10]
#print sort_list

# #第三步：写入html文件
htmlfile = open('log.html','w')
htmlfile.write('''<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<title>网站访问日志</title>
<style type="text/css">
div {color:blue;text-align:center;}
h1 {color:purple;text-align:center;}
table
{
border:2px solid black;
width:100%;
text-align:center;
font-family:arial;
color:red;
font-size:20px;
}
th
{
background-color:blue;
color:red;
}
td
{
height:50px;
vertical-align:center;
}
</style>
</head>
<body>
<div>
<h1>网站访问日志排行榜(前十)</h1>
</div>
<div>
<table border=1>
<tr>
    <th>按访问次数多少排序</th>
    <th>IP地址</th>
    <th>请求回显状态</th>
    <th>请求访问次数</th>
  </tr>\n''')
i = 1
for dict_key in sort_list:
    htmlfile.write('<tr><td>第 %d 名</td><td>%s</td><td>%s</td> <td>%s</td></tr> \n' %(i,sort_dict[dict_key][0],sort_dict[dict_key][1],dict_key))
    i += 1
htmlfile.write(''' </table>
</div>
</body>
</html>''')

htmlfile.close()
