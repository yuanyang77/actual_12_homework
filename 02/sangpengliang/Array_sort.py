#encoding=utf-8

arr =  [3,7,18,2,20,99,1,54,100,23,65,22,78]
count = 0
for j in arr:
    for i in range(len(arr)-1):
        count +=1
        if arr[i] > arr[i+1]:
            arr[i],arr[i+1] = arr[i+1],arr[i]
        print arr
        #print i,arr[i]

print count
print arr