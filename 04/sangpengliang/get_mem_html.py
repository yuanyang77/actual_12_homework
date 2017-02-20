#encoding=utf-8
def getMem():
# 指定参数读取行内容
    with  open('meminfo', 'r') as f:
        # 生成html文件
        htmlfile = open('index.html', 'w')
        htmlfile.write('''
        <html>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
        <title>内存信息统计</title>
        <body>
        <table border=1>
        <tr>
        <td align="center">&nbspMEMORY INFO&nbsp</td>
        <td align="center">&nbspNUM&nbsp</td>
        <td align="center">&nbspKB/MB&nbsp</td>
        </tr>
        ''')
        htmlfile.close()
        for line in f:
            if line == '\n':
                continue
            if line.split()[0] == 'MemTotal:':
                print 'System %s %s %s' % (line.split()[0], line.split()[1], line.split()[2])
                htmlfile = open('index.html', 'a+')
                htmlfile.write('<tr><td>%s</td><td  align="right">%s</td><td  align="left">%s</td></tr> \n' % (line.split(':')[0], line.split()[1], line.split()[2]))
                htmlfile.write('<tr><td>%s</td><td  align="right">%s</td><td  align="right">MB</td></tr> \n' % (line.split(':')[0], int(line.split()[1])/1024))
            if line.split()[0] == 'MemFree:':
                print 'System %s %s %s' % (line.split()[0], line.split()[1], line.split()[2])
                htmlfile = open('index.html', 'a+')
                htmlfile.write('<tr><td>%s</td><td  align="right">%s</td><td  align="left">%s</td></tr> \n' % (line.split(':')[0], line.split()[1], line.split()[2]))
                htmlfile.write('<tr><td>%s</td><td  align="right">%s</td><td  align="right">MB</td></tr> \n' % (line.split(':')[0], int(line.split()[1])/1024))
            if line.split()[0] == 'MemAvailable:':
                print 'System %s %s %s' % (line.split()[0], line.split()[1], line.split()[2])
                htmlfile = open('index.html', 'a+')
                htmlfile.write('<tr><td>%s</td><td  align="right">%s</td><td  align="left">%s</td></tr> \n' % (line.split(':')[0], line.split()[1], line.split()[2]))
                htmlfile.write('<tr><td>%s</td><td  align="right">%s</td><td  align="right">MB</td></tr> \n' % (line.split(':')[0], int(line.split()[1])/1024))
            if line.split()[0] == 'Buffers:':
                print 'System %s %s %s' % (line.split()[0], line.split()[1], line.split()[2])
                htmlfile = open('index.html', 'a+')
                htmlfile.write('<tr><td>%s</td><td  align="right">%s</td><td  align="left">%s</td></tr> \n' % (line.split(':')[0], line.split()[1], line.split()[2]))
                htmlfile.write('<tr><td>%s</td><td  align="right">%s</td><td  align="right">MB</td></tr> \n' % (line.split(':')[0], int(line.split()[1])/1024))
        htmlfile.write('''
        </body>
        </html>
        ''')
getMem()
