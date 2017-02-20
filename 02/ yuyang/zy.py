#!/usr/bin/python
# -*- coding: utf-8 -*-
import os 
import sys
import time

# **********************

# 2016年12月04日17:30:40

# yuyang Home work!!!!!! 

# **********************

# linux创建文件函数
def TouchFile():
    os.system('touch yuyang.txt')
    os.system('echo "111:python:123456">>yuyang.txt')
    os.system('echo "222:shell:1234567">>yuyang.txt')
    os.system('echo "333:perl:12345678">>yuyang.txt')



#windows创建文件
def WINTouchFile():

    os.system('@echo 111:python:123456>>yuyang.txt')
    os.system('@echo 222:shell:1234567>>yuyang.txt')
    os.system('@echo 333:perl:12345678>>yuyang.txt')
  

#查找文件是否存在不存在则创建
def Findfile(): 
    filename = r'yuyang.txt'
    if os.path.exists(filename):
        print ''
        print 'OK,the "%s" file exists' % filename
        print ''
    else:
        print ''
        print "Sorry, I cannot find the '%s' file" %filename
        print "..."
        os.system('sleep 1')
        Prompt = raw_input('Do you want to create a filename yuayng.txt.YES/NO:')
        if Prompt == 'yes' or Prompt == 'YES':
            TouchFile()
            os.system('sleep 1')
            print '.....'
            print 'Ok touch yuyang.txt Success!!!!'
            os.system('sleep 1')
        else:
            print 'Good Bey  ~~~~'
            sys.exit()
            
#Win查找文件是否存在不存在则创建
def WinFindfile(): 
    filename = r'yuyang.txt'
    if os.path.exists(filename):
        print 'OK,the "%s" file exists' % filename
    else:
        print "Sorry, I cannot find the '%s' file" %filename
        print "" 
        Prompt = raw_input('Do you want to create a filename yuayng.txt.YES/NO:')
        if Prompt == 'yes' or Prompt == 'YES':
            WINTouchFile()
            print ''
            print '....'
            time.sleep(1)
            print 'Ok touch yuyang.txt '
            print ''
        else:
            print 'Good Bey  ~~~~'
            sys.exit()
#上面都是没事练习玩的linux测试没问题 windows 如果不详

def start():
    while True:  
        TXT="""
        please must inpt 1~2!!!!! 
        1. linxu
        2. windows

        """
        Prompt = raw_input(TXT)
        if Prompt == '1':
            Findfile()
            break

        elif Prompt == '2':
            WinFindfile() 
            break
        else:
            print 'Must input 1 or 2'
            continue


#开始写作业 

def main():
   start() 
   Filename = open('yuyang.txt','r') 
   Space= Filename.read().split('\n')
   Filename.close()
   Space.pop() 
   User_list =Space[::]
   print 'welcome~~~'
   print ''
   print 'phone:user:password'
   print ''
   print User_list
   print ''
   shit = True
   while shit == True:
       _Users = raw_input('please input Users>')
       _Password = raw_input('please input Passwd>')
       Bad = None
       for Message in User_list:
           New_list = Message.split(':')
           if New_list[0] == _Users or New_list[1] == _Users:
               if New_list[2] == _Password:
                   print 'success login %s' % New_list[0]
                   Bad = True
                   shit = False
                   break
               else:
                    Bad = True
                    print 'password  error!!! '
       if not Bad:
           print 'user not fonud'
    
if __name__=="__main__":
    main()
            


