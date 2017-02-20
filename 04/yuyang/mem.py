mem.py
#!/usr/bin/python

import time

def getmem(memfile):
    mem_list = []
    mem_dic = {}
    user_mem = {}
    with open(memfile,'r') as mems:
        for x in mems:
            mem_list = x.split()
            mem_dic[mem_list[0]] = mem_list[1]
    for k in mem_dic:
        if k == 'MemTotal:':
            one = int(mem_dic[k])
        if k == 'MemFree:':
            two = int(mem_dic[k])
        if k == 'Buffers:':
            three = int(mem_dic[k])
    total = (one - two - three)/1000
    return '%sM' %total

def Times(sec):
    while True:
        print getmem('/proc/meminfo')
        time.sleep(sec)

Times(1)