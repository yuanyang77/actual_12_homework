SORT=[]
TMP=0
Alist = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]

while True:
    for i in Alist:
        if TMP == i:
            SORT.append(TMP)
    TMP += 1
    if len(Alist) == len(SORT):
        break
print SORT[-1],SORT[-2]
