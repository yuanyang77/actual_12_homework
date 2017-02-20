arr = [3,7,18,2,500,12,1320,56,99,132,45,366]
count = 0
for j in range(len(arr)-1):
    for i in range(len(arr)-1-j):
        count +=1
        if arr[i]>arr[i+1]:
           arr[i],arr[i+1]=arr[i+1],arr[i]
print count
print arr
