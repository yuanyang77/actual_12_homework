# coding=utf-8
import time

def getmen():
    with open('meminfo', 'r') as file:
        totle = int(file.readline().split()[1])
        free = int(file.readline().split()[1])
        buffers = int(file.readline().split()[1])
        cached = int(file.readline().split()[1])
        mem_use = totle - free - buffers - cached
    return mem_use
while True:
    print 'MenUsed:  %s kB' % getmen()
    time.sleep(1)