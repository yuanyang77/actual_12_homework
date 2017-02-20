

L = [9,8,7,6,5,4,3,2,1]
print L

for x in range(1,len(L)):
    for i in range(0,len(L)-x):
        if L[i] > L[i+1]:
            L[i],L[i+1] = L[i+1],L[i]
    print L 
