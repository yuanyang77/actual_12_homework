#encoding:utf -8
#读文件，并根据ip和status出现的次数生成dict
def Statistics(html_name):
    res_dict = {}
    with open(html_name,'r') as f:
        for line in f:
            if line == '\n':
                continue
            temp = line.split()
            tup = (temp[0],temp[8])
            res_dict[tup] = res_dict.get(tup,0) +1
    return res_dict
#将生成内容写入文件
def Generate_html(res_list,index_name='index.html'):
    html_str = '<table border="1">'
    tr_str = '<tr><td>%s</td><td>%s</td><td>%s</td></tr>'
    html_str += tr_str%('IP','status','count')
    for ip in res_list[:-11:-1]:
        html_str += tr_str%(ip[0][0],ip[0][1],ip[1])
    html_str +='</table>'
    with open(index_name,'w') as f:
        f.write(html_str)

res_dict = Statistics('www_access_20140823.log')
res_list = sorted(res_dict.items(),key=lambda x:x[1])
Generate_html(res_list,'index.html')
