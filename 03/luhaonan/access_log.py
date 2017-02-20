#coding=utf-8

# 作业
# 一个access_log（直接发群里），按照ip和访问状态两个维度统计数据，打印前十名，并且以html表格的形式展现
# 每一行大概是这样
# 61.159.140.123 - - [23/Aug/2014:00:01:42 +0800] "GET /favicon.ico HTTP/1.1" 404 \ "-" "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.66 Safari/537.36 LBBROWSER" "-"

# 提示
# s = '61.159.140.123 - - [23/Aug/2014:00:01:42 +0800] "GET /favicon.ico HTTP/1.1" 404 \ "-" "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.66 Safari/537.36 LBBROWSER" "-"'
# print s.split()[0]
# print s.split()[8]

# -----------------菜鸡方式功能实现-----------------
# 读取文件,存入字典log_dict
log_dict = {}
try:
    file = open('www_access_20140823.log', 'r')
    try:
        for line in file.readlines():
            if line == '\n':
                continue
            temp = (line.split()[0], line.split()[8])
            log_dict[temp] = log_dict.setdefault(temp, 0)+1
    except:
        pass
except IOError as err:
    print "Error: 没有找到文件或读取文件失败!"+str(err)
finally:
    file.close()
# print log_dict
print "读取文件到字典完成..."

# 冒泡排序
res_list = log_dict.items()
# print res_list
for i in range(len(res_list)):
    for j in range(i+1, len(res_list)):
        if res_list[i][1] < res_list[j][1]:
            res_list[i], res_list[j] = res_list[j], res_list[i]
# print res_list
print "排序完成..."

# 取次数最多的前十写入html
count = 0
try:
    w = open('accesslog.html', 'w')
    try:
        w.write('''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>访问日志排名前十IP及Status</title></head><body><table border='1'><tr><td>IP</td><td>STATUS</td><td>COUNT</td></tr>''')
        for i in res_list:
            if count >= 10:
                break
            temp = '<tr><td> %s </td><td> %s </td><td> %s </td></tr>' % (i[0][0], i[0][1], i[1])
            # print temp
            count += 1
            w.write(temp)
        w.write('''</table></body></html>\n''')
    except:
        pass
except IOError:
    print "Error: 没有找到文件或读取文件失败!"
finally:
    w.close()
print "结果写入html完成..."


# -----------------百度、Google后逼格提升并且不知道对不对的结果-----------------
log_dict = {}
# 读取文件,使用with as方式,用来代替传统的try...finally...语法
with open('www_access_20140823.log', 'r') as file:
    for line in file.readlines():
        if line == '\n':
            continue
        # 获取ip、状态,以元组方式为key,记数存入dict
        temp = (line.split()[0], line.split()[8])
        log_dict[temp] = log_dict.setdefault(temp, 0)+1

print "读取文件到字典完成..."

# 使用sorted及匿名函数进行排序
log_dict = sorted(log_dict.iteritems(), key=lambda d:d[1], reverse=True)
print "排序完成..."

# 取前统计次数排名前十写入html
with open('accesslog.html', 'w') as file:
    file.write('''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>访问日志排名前十IP及Status</title></head><body><table border='1'><tr><td>IP</td><td>STATUS</td><td>COUNT</td></tr>''')
    count = 1
    for i in log_dict:
        if count > 10:
            break
        temp = '<tr><td> %s </td><td> %s </td><td> %s </td></tr>' % (i[0][0], i[0][1], i[1])
        file.write(temp)
        count += 1
    file.write('''</table></body></html>\n''')
print "结果写入html完成..."
