n=int(input())
f=[]
m=[]
s=''
for i in range(0,n):
    x=input().split('.')
    if(x[0]=='f'):
        s=x[1]
        s=s[0].upper()+s[1:].lower()
        t=(s,x[2])
        f.append(t)
        s=''
    else:
        s=x[1]
        s=s[0].upper()+s[1:].lower()
        t=(s,x[2])
        m.append(t)
        s=''
        
f=sorted(f,key =lambda item :(item[0],item[1]))
m=sorted(m,key =lambda item :(item[0],item[1]))
#print(f)
#print(m)    
for i in f:
    print('f %s %s' %(i[0],i[1]))
for i in m:
    print('m %s %s' %(i[0],i[1]))