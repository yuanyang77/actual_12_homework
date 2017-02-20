#encoding:utf8
list_t =  [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
a = 0
b = 0
for i in list_t:
    if i > a:
        a,b = i,a
print 'max is %s,sencond is %s'%(a,b)
