#encoding=utf-8
from __future__ import print_function
from collections import OrderedDict
def get_Mem():
    meminfo = OrderedDict()
    with  open('meminfo','r') as f:
        for line in f:
            meminfo[line.split(':')[0]] = line.split(':')[1].strip()
    return meminfo
if __name__ == '__main__':
    meminfo = get_Mem()
    print("Total memory:{}".format(meminfo['MemTotal']))
    print("Total memory:{}".format(meminfo['MemFree']))
    print("Total memory:{}".format(meminfo['MemAvailable']))
    print("Total memory:{}".format(meminfo['Buffers']))

    # 生成html文件
    htmlfile = open('indexs.html', 'w')
    htmlfile.write('''
    <html>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <title>内存信息统计</title>
    <body>
    <table border=1>
    <tr>
    <td align="center">MEMORY INFO</td>
    </tr>
    ''')
    htmlfile.close()
    htmlfile = open('indexs.html', 'a+')
    htmlfile.write('<tr><td>%s</td></tr> \n' % ("Total memory:{}".format(meminfo['MemTotal'])))
    htmlfile.write('<tr><td>%s</td></tr> \n' % ("Total memory:{}".format(meminfo['MemFree'])))
    htmlfile.write('<tr><td>%s</td></tr> \n' % ("Total memory:{}".format(meminfo['MemAvailable'])))
    htmlfile.write('<tr><td>%s</td></tr> \n' % ("Total memory:{}".format(meminfo['Buffers'])))

    htmlfile.write('''
    </body>
    </html>
    ''')
    htmlfile.close()