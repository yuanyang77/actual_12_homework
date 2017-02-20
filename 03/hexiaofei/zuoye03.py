# -*-coding:utf-8-*-

#创建一个空dict
logfile_dict = {}

#读取日志文件，把空行排除了,取日志文件第1个和第8个值,logfile_dict最终结果是这样的
#{('101.226.167.201', '200'): 1, ('113.7.255.88', '200'): 1}
#readlines()读取全部内容
#split把字符串切割为list
#setdefault 设置默认值，和get类似

file = open('www_access_20140823.log', 'r')
for line in file.readlines():
    if line == '\n':   
          continue
    temp = (line.split()[0], line.split()[8])
    logfile_dict[temp] = logfile_dict.setdefault(temp, 0)+1
    file.close()
#print logfile_dict

#将dict转成list  items()
#re_list最终结果为  [(('101.226.167.201', '200'), 1), (('113.7.255.88', '200'), 1)]
res_list = logfile_dict.items()

#排序
for i in range(len(res_list)):
    for j in range(i+1,len(res_list)):
        if res_list[i][1] < res_list[j][1]:
            res_list[i], res_list[j] = res_list[j], res_list[i]
#print res_list


#写入到log.html
count = 0
w = open('log.html', 'w')
w.write('''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>访问日志排名前十IP及Status</title></head><body><table border='1'><tr><td>IP</td><td>STATUS</td><td>NUM</td></tr>''')
for k in res_list:
    if count >= 10:
      break
    temp = '<tr><td> %s </td><td> %s </td><td> %s </td></tr>' % (k[0][0], k[0][1], k[1])
#print temp
    count += 1
    w.write(temp)
w.write('''</table></body></html>\n''')

w.close()
