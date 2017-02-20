#!/usr/bin/env python
# _*_ coding:utf-8 _*_

#1.回顾冒泡代码

arr = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]

count = len(arr)

print '冒泡排序前的结果:',arr,'\n'

for i in range(0,count):
    for j in range(i+1,count):
        if arr[i] < arr[j]:
            swap = arr[i]
            arr[i] = arr[j]
            arr[j] = swap
            #arr[i],arr[j] = arr[j],arr[i]
print '冒泡排序后的结果:',arr,'\n'



#2.插入排序 归并排序 快速排序（了解概念）
#2.1  插入排序
"""
描述

插入排序的基本操作就是将一个数据插入到已经排好序的有序数据中，从而得到一个新的、个数加一的有序数据，算法适用于少量数据的排序，时间复杂度为O(n^2)。是稳定的排序方法。插入算法把要排序的数组分成两部分：第一部分包含了这个数组的所有元素，但将最后一个元素除外（让数组多一个空间才有插入的位置），而第二部分就只包含这一个元素（即待插入元素）。在第一部分排序完成后，再将这个最后元素插入到已排好序的第一部分中。
"""


"""
2.2、归并排序

描述

归并排序是建立在归并操作上的一种有效的排序算法,该算法是采用分治法（Divide and Conquer）的一个非常典型的应用。将已有序的子序列合并，得到完全有序的序列；即先使每个子序列有序，再使子序列段间有序。若将两个有序表合并成一个有序表，称为二路归并。

归并过程为：比较a[i]和a[j]的大小，若a[i]≤a[j]，则将第一个有序表中的元素a[i]复制到r[k]中，并令i和k分别加上1；否则将第二个有序表中的元素a[j]复制到r[k]中，并令j和k分别加上1，如此循环下去，直到其中一个有序表取完，然后再将另一个有序表中剩余的元素复制到r中从下标k到下标t的单元。归并排序的算法我们通常用递归实现，先把待排序区间[s,t]以中点二分，接着把左边子区间排序，再把右边子区间排序，最后把左区间和右区间用一次归并操作合并成有序的区间[s,t]。
"""

"""
2.3、快速排序

描述

通过一趟排序将要排序的数据分割成独立的两部分，其中一部分的所有数据都比另外一部分的所有数据都要小，然后再按此方法对这两部分数据分别进行快速排序，整个排序过程可以递归进行，以此达到整个数据变成有序序列。
"""
f = open('psname.txt','r')
arr = f.read().split('\n')

name = raw_input("请输入用户名或手机号:")
pwd = raw_input("请输入密码:")

phone_list = []
user_list = []
pwd_list = []

for login in arr:
    temp = login.split(':')
    phone_list.append(temp[0])
    user_list.append(temp[1])
    pwd_list.append(temp[2])
    if name in phone_list or name in user_list:
        if pwd in pwd_list:
            print '登陆成功!'
        else:
            print '密码错误!'
        break
f.close(



)
