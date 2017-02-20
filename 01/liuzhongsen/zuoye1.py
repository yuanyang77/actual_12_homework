#!/usr/bin/env python

arr = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]

count = len(arr)

for i in range(0,count):
    for j in range(i+1,count):
        if arr[i] < arr[j]:
            #swap = arr[i]
            #arr[i] = arr[j]
            #arr[j] = swap
            arr[i],arr[j] = arr[j],arr[i]
   
print 'bubble sort later',arr

print 'max two values is:',arr[0],arr[1]
