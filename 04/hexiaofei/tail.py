#-*-coding:utf-8-*-
# 用open打开文件
# 用seek文件指针，跳到文件最后面
# while True进行循环
# 持续不停的readline，如果能读到内容，打印出来即可
#seek(移动的字符，移动的相对位置【0是文件开始，1是现在的位置，2是文件结尾】)

def my_tail(name):
    with open(name) as f:
      f.seek(0,2)
      while True:
	 last_line =f.tell()
	 line = f.readline()
	 if line:
	    print line


my_tail(name='test.txt')
