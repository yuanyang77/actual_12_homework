#!/usr/bin/env python
# -*- coding: utf-8 -*-
#   author:RaoPeng

import time

#函数功能:获取内存信息,返回字典
def getMem(file_name):
    count = 0
    res_dict = {}
    with open(file_name) as f:
        for line in f:
            if line=='\n':
                continue
            temp = line.split()
            res_dict[temp[0]] = temp[1]
            count += 1
            if count>=4:
                break
    return res_dict

#函数功能:计算内存的使用量,并返回计算结果
def calculate_Mem():
    res_dict = getMem('/proc/meminfo')
    mem_used = int(res_dict['MemTotal:'])-int(res_dict['MemFree:'])-int(res_dict['Buffers:'])-int(res_dict['Cached:'])
    return mem_used

count = 0
while count<50:
    print calculate_Mem()
    count += 1
    time.sleep(1)
