#encoding:utf-8
a = 0
b = 0
_list = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
for i in _list:
    if a < i:
        a = i

for i in  _list:
    if i == a:
        continue
    if i > b:
        b = i
print a,b
