arr = [10,9,8,7,6,5,4,3,2,1]
print arr
count = 0
for j in range(len(arr)):
    for i in range(len(arr) - 1 - j ):
        count += 1
        if arr[i] > arr[i+1]:
            arr[i],arr[i+1] = arr[i+1],arr[i]
            print arr
print arr,count 
