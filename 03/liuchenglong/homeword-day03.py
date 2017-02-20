f = open('www_access_20140823.log','r')
res=[]
res_dic={}
sort_res=[]
for line in f:
	if line.split():
		ip,state = line.split()[0],line.split()[8]
		res.append((ip,state))
for i in res:
	res_dic[i]=res_dic.get(i,0)+1
for j in res_dic:
	sort_res.append([j,res_dic[j]])
for y in range(10):
	for x in range(0,len(sort_res)-1-y):
		if sort_res[x][1]>sort_res[x+1][1]:
			sort_res[x],sort_res[x+1] = sort_res[x+1],sort_res[x]
res_html = open('top.html','w+')
res_html.write('''<html>
	<body>
		<table border='1' align="center">
			<tr align="center">
				<td width="50" >RANKING</td>
				<td width="200" >IP</td>
				<td width="80">STATE</td>
				<td width="50">COUNT</td>
			</tr>''')
for ranking in range(1,11):
	res_html.write('''			
			<tr align="center">
				<td width="50" >'''+str(ranking)+'''</td>
				<td width="100" align="left" style="padding-left:50px;" >'''+str(sort_res[-ranking][0][0])+'''</td>
				<td width="80">'''+str(sort_res[-ranking][0][1])+'''</td>
				<td width="50">'''+str(sort_res[-ranking][1])+'''</td>
			</tr>''')
res_html.write('''
		</table>
	</body>
</html>''')
#for line in sort_res[-1:-11:-1]:
#	res_html.write(str(line[0][0])+':'+str(line[0][1])+':'+str(line[1])+'\n')
res_html.close()
#print sort_res[-1:-11:-1]
	
