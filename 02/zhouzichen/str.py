
#arr = ['user:pwd','user1:pwd1','user2:123']
#print arr

f = open('test.txt')
login_info = f.read().split('\n')
f.close()
print login_info

input_user = raw_input('please input your user name or cellphone num :')
input_passwd = raw_input('please input your passwd :')

i = 0
while True:
    if i <= len(login_info) - 1 :
        if input_user == login_info[i].split(':')[0] or input_user == login_info[i].split(':')[1]:
            if input_passwd == login_info[i].split(':')[2]:
                print "yes"
                break
            else:
                print "sec wrong"
                break
        i += 1
    else :
        print 'No such user'
        break

        
    
    
