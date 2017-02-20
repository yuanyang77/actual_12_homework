#!/usr/bin/python
# -*- coding: utf-8 -*-

# http://blog.csdn.net/onlyanyz/article/details/45177643  参考的算法讲解
# pycharm技巧：  选中 ctrl+/ 批量注释  ctrl+d  快速复制  ctrl+e 快速删除 shift+enter 快速换行  ctrl+alt+l 遵守PEP8编码规范的格式化
# 方法1


unsortedList = [1 , 2 , 3 , 2 , 12 , 3 , 1 , 3 , 21 , 2 , 2 , 3 , 4111 , 22 , 3333 , 444 , 111 , 4 , 5 , 777 , 65555 ,
                45 , 33 , 45]


def bubbleSort(unsortedList):
    list_length = len(unsortedList)
    for i in range(0 , list_length - 1):
        for j in range(0 , list_length - i - 1):
            if unsortedList[j] > unsortedList[j + 1]:
                unsortedList[j] , unsortedList[j + 1] = unsortedList[j + 1] , unsortedList[j]
    return unsortedList


print(bubbleSort(unsortedList)[-2:])

# 方法2
unsortedList = [1 , 2 , 3 , 2 , 12 , 3 , 1 , 3 , 21 , 2 , 2 , 3 , 4111 , 22 , 3333 , 444 , 111 , 4 , 5 , 777 , 65555 ,
                45 , 33 , 45]
for i in sorted(unsortedList)[-2:]:
    print(i)

