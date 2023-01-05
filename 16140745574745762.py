n=0
n=input()
n=int(n)
d=dict()
l=[]
s=''
khorogi=''
for i in range(0,n):
    x=input()
    m=x.split()
    d[m[0]]=m[1]
   

y=input()
yy=y.split()
for j in range(0,len(yy)):
    s=d.get(yy[j],yy[j])
    l.append(s)
    
for i in range(0,len(l)):
    khorogi=khorogi+l[i]+' '
khorogi=khorogi.strip()
print(khorogi)    