f=open('www_access_20140823.log','r')
result={}
for line in f:
    if line!='\n':
        combo=line.split()[0]+'-'+line.split()[8]
        if combo in result:
            result[combo]+=1
        else:
            result[combo]=1
f.close()
#print result
resultlist=[]
for key,value in result.items():
    resultlist.append([value,key])
#print resultlist
for i in range(len(resultlist)-1):
    for j in range(len(resultlist)-1-i):
        if resultlist[j][0]>=resultlist[j+1][0]:
            resultlist[j],resultlist[j+1]=resultlist[j+1],resultlist[j]
#print resultlist
f=open('result.html','w')
txt='<table border="1">'
f.write(txt)

for i in range(10):
    tmp=resultlist.pop()
    f.write('<tr>')
    f.write('<td>'+str(tmp[0])+'</td>')
    f.write('<td>'+tmp[1].split('-')[0]+'</td>')
    f.write('<td>'+tmp[1].split('-')[1]+'</td>')
    f.write('/<tr>')


txt='''
</table>
'''
f.write(txt)
f.close()
