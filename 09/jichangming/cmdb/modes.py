#encoding:utf -8
user_dict = {}
def user_list():
    with open('user.txt','r') as f:
        for user in f.read().split('\n'):
            temp = user.split(':')
            if user:
                user_dict[temp[0]]= temp[1]
    return user_dict

def user_write():
    file_arr = []
    for user,pwd in user_dict.items():
        file_arr.append('%s:%s'%(user,pwd))
    with open('user.txt','w') as f:
        f.write('\n'.join(file_arr))