#!/usr/bin/env python
# -*- coding: utf-8 -*-
#   author: RaoPeng
f = open('www_access_20140823.log')
dic = {}
res_dic = {}
for i in f:
	temp = (i.split(' ')[0],i.split(' ')[8])
	dic[temp] = dic.get(temp,0)+1

#反转dic,把出现的次数当成key
for k in dic:
	res_dic[dic[k]] = res_dic.get(dic[k],[])+[k]

#排序，取前十,在这里还是采用冒泡来排序
count_arr = res_dic.keys()
for i in range(10):
	for j in range(len(count_arr)-1):
		if count_arr[j]>count_arr[j+1]:
			count_arr[j],count_arr[j+1] = count_arr[j+1],count_arr[j]
#print count_arr[-10:]
f = open('homework.html','a+')
f.write("<table border='1'>\n\t<tr>\n\t\t<td>IP</td>\n\t\t<td>STATUS</td>\n\t\t<td>COUNT</td>\n\t</tr>")
count = 0
while count<10:
	val = count_arr.pop()
	for k in res_dic[val]:
		f.write("\n\t<tr>\n\t\t<td>%s</td>\n\t\t<td>%s</td>\n\t\t<td>%s</td>\n\t</tr>" %(k[0],k[1],val))
		#print 'ip %s,status %s,count is %s' %(k[0],k[1],val)
		count += 1
f.close()
#print res_dic
#for i in res_dic:
#	print '%s--------->%s' %(i,res_dic[i])
f.close()
