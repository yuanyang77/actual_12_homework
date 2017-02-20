#!/usr/bin/env python
#coding:utf-8
L = [6,12,11,5,17,15,8,3,20]

def merge(L):
    if len(L) == 1:
        return L
    mid = len(L)/2
    left = merge(L[:mid])
    right = merge(L[mid:])

    i=0
    j=0
    k=0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            L[k] = left[i]
            i += 1
            k += 1
        else:
            L[k] = right[j]
            j += 1
            k += 1
    remain = left if i<j else right
    r = i if remain == left else j

    while r< len(remain):
        L[k] = remain[r]
        r += 1
        k += 1
    print L
    return L

print merge(L)
