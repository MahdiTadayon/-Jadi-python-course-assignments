n=int(input())
d={}
for i in range(0,n):
    x=input().split()
    
    d[x[1]]=x[0]
    d[x[2]]=x[0]
    d[x[3]]=x[0]
    #print(x)
#print(d)    
s=''
y=input().split()   
#print(y) 
for i in y:
    s=s+d.get(i,i)+' '
print(s)    
    
