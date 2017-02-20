#encoding=utf-8

def getMem():
#读取前5行
    f = open('meminfo', 'r')
    print "==========有空格=============="
    for line in f.readlines()[0:4]:
        line = line.strip('\n')
        print line
    print "==========无空格=============="
    f = open('meminfo', 'r')
    for line in f.readlines()[0:4]:
        line = line.strip('\n')
        no_line = ' '.join(line.split())
        print no_line
    print '='*6 + "指定参数读取行内容" + '='*6
#指定参数读取行内容
    with  open('meminfo','r') as f:
        for  line in f:
            if line == '\n':
                continue
            if line.split()[0] == 'MemTotal:':
                print 'System %s  is %s %s' % (line.split()[0],line.split()[1],line.split()[2])
            if line.split()[0] == 'MemFree:':
                print 'System %s  is %s %s' % (line.split()[0], line.split()[1],line.split()[2])
            if line.split()[0] == 'MemAvailable:':
                print 'System %s  is %s %s' % (line.split()[0], line.split()[1],line.split()[2])
            if line.split()[0] == 'Buffers:':
                print 'System %s  is %s %s' % (line.split()[0], line.split()[1],line.split()[2])
getMem()
print '='*30







