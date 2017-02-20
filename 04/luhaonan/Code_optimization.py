# coding=utf-8

def read_file(filename):
    log_dict = {}
    with open(filename, 'r') as file:
        for line in file.readlines():
            if line == '\n':
                continue
            # 获取ip、状态,以元组方式为key,记数存入dict
            temp = (line.split()[0], line.split()[8])
            log_dict[temp] = log_dict.setdefault(temp, 0)+1
    print "读取文件到字典完成..."
    return log_dict
# 根据方法传入参数统计对应数量的top写入html
def generate_html(log_list, top=10):
    html_str = '''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>访问日志排名前十IP及Status</title></head><body><table border='1'>'''
    tr_tmp = '<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>'
    html_str += tr_tmp % ('ID', 'IP', 'STATUS', 'COUNT')
    res = 1
    for (ip, status), count in log_list:
        if res > top:
            break
        html_str += tr_tmp % (res, ip, status, count)
        res += 1
    html_str += '</table></body></html>\n'
    with open('accesslog.html', 'w') as file:
        file.write(html_str)
    print "结果写入html完成..."

log_dict = read_file('www_access_20140823.log')
log_list = sorted(log_dict.iteritems(), key=lambda d: d[1], reverse=True)
generate_html(log_list, 12)