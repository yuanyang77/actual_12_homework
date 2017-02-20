f = open('01.txt')
arr = f.read().split('\n')
f.close()
user = 'user2'
pwd = 'pwd2'
exist = True
for i in arr[0:len(arr)-1]:
    if i.split(':')[0] == user or i.split(':')[1] == user:
        if i.split(':')[2] == pwd:
            print 'login success'
        else:
            print 'wrong pwd'
        exist = False
        break
if exist:
    print 'no user'
