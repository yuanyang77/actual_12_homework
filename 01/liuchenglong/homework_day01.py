#get the maximum two numbers in the list
list= [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45,65555]
max_1=0
max_2=0

#the first method
for x in list:
	if x>max_1:
		max_2=max_1
		max_1=x
	elif x>max_2:
		max_2=x
'''		
#this following method is inappropriate if the list has two or more same maximum 

for x in list:
	if x>max_1:
		max_1=x
for y in list:
	if y == max_1:
		continue
	if y>max_2:
		max_2=y

#this method is ok,but it change the list
for x in list:
	if x>max_1:
		max_1=x
list.remove(max_1)
for y in list:
	if y>max_2:
		max_2=y
'''		
print'the maximum two numbers are %s , %s '%(max_1,max_2)
