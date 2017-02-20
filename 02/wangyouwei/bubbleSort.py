#!/usr/bin/python
# -*- coding: utf-8 -*-

import random

unsortedList = []


# generate an unsorted list
def generateUnsortedList(num):
    for i in range(0 , num):
        unsortedList.append(random.randint(0 , 100))
    print unsortedList


# 冒泡排序
def bubbleSort(unsortedList):
    list_length = len(unsortedList)
    for i in range(0 , list_length - 1):
        for j in range(0 , list_length - i - 1):
            if unsortedList[j] > unsortedList[j + 1]:
                unsortedList[j] , unsortedList[j + 1] = unsortedList[j + 1] , unsortedList[j]
    return unsortedList


generateUnsortedList(10)
print bubbleSort(unsortedList)

