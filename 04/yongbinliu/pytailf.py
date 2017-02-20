#coding=utf8
import time

def pytailf(file='/var/log/messages'):
	with open(file,'r') as f:
		f.seek(0,2)
		while True:
			line=f.readline()
			if  line:
				print line,
			time.sleep(0.01)



if __name__=='__main__':
	pytailf()
