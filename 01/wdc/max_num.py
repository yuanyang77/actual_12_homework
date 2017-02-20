#encoding:utf-8

list = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]

max_num_one = list[0]   # 防止出现负数，初始值不为零
max_num_two = list[0]

for i in list:
    if i > max_num_one:
        max_num_two = max_num_one
        max_num_one = i
    elif i > max_num_two and i < max_num_one:
        max_num_two = i
print max_num_two, max_num_one
