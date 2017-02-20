#!/usr/bin/env python
#coding:utf-8
L = [2,9,8,7,6,5,4,1,3]
print L

def quick(L,left,right):
    if left >= right:
        return L
    key = L[left]
    low = left
    high = right
    while left < right:
        while left < right and L[right] >= key:
            right -= 1
        L[left] = L[right]                     #------------------ 比key值小的值放到左边
        #print L
        while left <right and L[left] <= key:
            left += 1
        L[right] = L[left]                     #------------------比key值大的放到右边
        #print L 
    #print L 
    #left = right 跳出循环
    L[left] = key                             #------------------将key值赋给left=right的位置
    #此时left=right,分别对左右子列表进行快速排序
    quick(L,low,right-1)
    quick(L,left+1,high)
    #递归调用，知道子列表为单一子列表 left=right
quick(L,0,len(L)-1)
#L.sort()
print L

