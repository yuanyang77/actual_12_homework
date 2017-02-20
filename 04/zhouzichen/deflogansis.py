#!/usr/bin/env python
# -*- coding:utf-8 -*-

def static_file(filename):
	with  open(filename, 'r') as f:
		d = {}
		while True:
			line = f.readline()
			if line ==  '' :
				break
			temp = (line.split()[0],line.split()[8])
			d[temp] = d.get(temp,0) + 1
	return d

def generate_html(sort_list):
	with open('www.html', 'w') as w:
		w.write('<table border="1"><tr><td>SourceIp</td><td>HttpCode</td><td>Count</td></tr>')
		for (ip,status),count in sort_list[-1:-10:-1]:
				w.write('<tr><td>%s</td><td>%s</td><td>%s</td></tr>' % (ip,status,count))
		w.write('</table>\n')

sort_dict = static_file('www_access_20140823.log')
tosort_list = sorted(sort_dict.items(),key=lambda x:x[1])
generate_html(tosort_list)