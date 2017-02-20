#!/usr/bin/env python
# -*- coding:utf-8 -*-

f = open('www_access_20140823.log', 'r')
d = {}
while True:
	line = f.readline()
	if line ==  '' :
		break
	line_splitkey = line.split()[0] + ':' + line.split()[8]
	if line_splitkey  in d :
		d[line_splitkey] += 1
	else :
		d[line_splitkey]  = 1
f.close()

sort_dict = {}
sort_list = []
for i in d :
	sort_dict[d[i]] = sort_dict.get(d[i], []) + [i]
	sort_list.append(d[i])
sort_list.sort()
count = 0

w = open('sum_table.html', 'w')
w.write('<table border="1"><tr><td>SourceIp</td><td>HttpCode</td><td>Count</td></tr>')
while count < 10:
	num = sort_list.pop()
	for k in sort_dict[num]:
		w.write('<tr><td>%s</td><td>%s</td><td>%s</td></tr>' % (k.split(':')[0], k.split(':')[1], num))
		count += 1
w.write('</table>\n')
w.close()
