#encoding=utf-8

#def my_tail():
#    with open('1.txt') as f:
#        f.seek(0,2)
#        while True:
#	        last_line =f.tell()
#	        line = f.readline()
#	        if line:
#	            print line
#my_tail()

import os
def tail(file_name):
    os.system('tail -f '+file_name)
tail('1.txt')
