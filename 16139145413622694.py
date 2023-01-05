
c=0
l=[]
l_j=[]
max_maghsom=0
for i in range(0,20):
    x=int(input())
    l.append(x)
    for i in range(1,x+1):
        if(x%i==0):
            c+=1 
    l.append(c)              
    c=0
for i in range(0,20):
    if(l[2*i+1]>=max_maghsom):
        max_maghsom=l[2*i+1]
for i in range(0,40):
    if(l[i]==max_maghsom):
        l_j.append(l[i-1])
print(max(l_j),max_maghsom)
        







