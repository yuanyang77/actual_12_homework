#encoding=utf-8
#方法1
#m = 0
#n = 0
#for i in [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]:
#    if i > m:
#        m = i
#for i in [1, 2, 3, 2, 12, 3, 1, 3, 21, 2, 2, 3, 4111, 22, 3333, 444, 111, 4, 5, 777, 65555, 45, 33, 45]:
#    if i != m and n < i:
#        n = i
#
#print m
#print n
#
#方法二
sum = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
max_first = sum[0]
max_second = sum[0]

for sum_num in sum:
    if max_first < sum_num :
        max_first = sum_num
for sum_num in sum:
    if sum_num != max_first and max_second < sum_num:
        max_second = sum_num
print max_first,max_second
