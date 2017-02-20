#encoding: utf-8
import time
def getMem(src):
    mem = {}
    with open(src,'r') as f:
        for line in f:
            if line == '\n':
                continue
            name = line.split(':')[0]
            var = line.split(':')[1].split()[0]
            #mem[name] = long(var) * 1024.0
            mem[name] = int(var)
    print 'MemTotal: %s'%mem['MemTotal']
    print 'MemFree: %s'%mem['MemFree']
    print 'Buffers: %s'%mem['Buffers']
    print 'Cached: %s'%mem['Cached']


if __name__ == '__main__':
    file_path = '/proc/meminfo'
    while True:
       time.sleep(1)
       print '-'*10 + time.strftime("%Y-%m-%d %X",time.localtime()) + '-'* 10
       getMem(file_path)


