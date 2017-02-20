#encoding:utf -8
#3. 实战函数tail  ，完成tail -f的功能
#import time
#time.sleep(1)暂停一秒

import time
def tails():
     while True:
        num = raw_input('Please input something: ')
        with open('tails.txt','a+') as f:
            f.write(num)
            f.write('\n')
            f.flush()
        time.sleep(1)
tails()