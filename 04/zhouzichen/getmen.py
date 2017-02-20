#!/usr/bin/env python
#coding:utf-8
import time

def getmem(lines=1):
	temp = ''
	with open('/proc/meminfo','r') as file:
		while lines > 0:
			temp += file.readline()
			lines -= 1
	return temp

def sleprint(func,funcarg):
    time.sleep(1)
    #print '-'*17 + 'meminfo'+ '-'*17
    print 'meminfo'.center(40,'-')
    print func(funcarg),
    print '-'*40

if __name__ == '__main__':
	while True:
		sleprint(getmem,4)
	
