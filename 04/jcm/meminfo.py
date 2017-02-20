#encoding:utf -8
#2.作业获取内存的函数 getMem（）
#    内存数据都在/proc/meminfo文件里
def getMen():
    with open('meminfo','r') as f:
        for line in f:
            if line =='\n':
                continue
            if line.split()[0] == 'MemTotal:':
                print 'System %s memory  is %s ' %(line.split()[0],line.split()[1])
            if line.split()[0]== 'MemFree:':
                print 'System %s memory  is %s ' %(line.split()[0],line.split()[1])
            if line.split()[0]== 'SwapTotal:':
                print 'System %s memory  is %s ' %(line.split()[0],line.split()[1])
getMen()