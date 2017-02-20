#coding=utf8
import time

def getmeminfo():
	with open('/proc/meminfo','r') as f:
		print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
		for i in range(4):
			print f.readline(),

if __name__=='__main__':
	while True:
		getmeminfo()
		time.sleep(1)
