#coding:utf-8

def get_top(src,top=10):
    line_list = []
    stat_dict = {}
    with open(src,'rb') as f:
        for line in f:
            if line == '\n':
                continue
            line_list = line.split()
            key = (line_list[0],line_list[6],line_list[8])
            stat_dict[key] = stat_dict.setdefault(key,0) + 1
    result = sorted(stat_dict.items(),key = lambda x:x[1])
    return result[:-top-1:-1]





if __name__ == '__main__':
    accesslog = 'access.log'
    result = get_top(accesslog,20)
    # for line in result:
    #      print line
    tbody = ''
    for line in result:
        tbody += '''<tr>
                <td>{ip}</td>
                <td>{url}</td>
                <td>{code}</td>
                <td>{count}</td>
                </tr>'''.format(ip=line[0][0],url=line[0][1],code=line[0][2],count=line[1])
    html = '''<!DOCTYPE html>
                <html>
                    <head>
                        <meta charset="utf-8"/>
                        <title>我是一个页面</title>
                    </head>
                    <body>
                        我是haining
                        <table border="1">
                            <thead>
                                <tr>
                                    <th>IP</th>
                                    <th>URL</th>
                                    <th>状态码</th>
                                    <th>次数</th>
                                </tr>
                            </thead>
                            <tbody>
                                {tbody}
                            </tbody>

                        </table>
                    </body>
                </html>
        '''.format(tbody=tbody)
    fh = open('top10.html','wb')
    fh.write(html)
    fh.close()
