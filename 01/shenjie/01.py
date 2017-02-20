list_num=[1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45,5000,10000]
max_num1=0
max_num2=0

for num in list_num:
    if num > max_num1:
            max_num1=num
    elif num == max_num1:
            continue
    elif num > max_num2:
            max_num2=num



print(max_num1)
print(max_num2)

