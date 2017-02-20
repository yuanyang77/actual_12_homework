#coding=utf-8
arr = [3,100,111,7,18,2,20,99,1,54,33,8]
for j in arr:
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            arr[i],arr[i+1] = arr[i+1],arr[i]
print arr
