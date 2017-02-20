#encoding: utf-8
path = 'a.log'
fhandler = open(path,'r')
fhandler.seek(0,2)
line = ''
while True:
    line = fhandler.readline()
    if line.endswith('\n'):
        print line,
