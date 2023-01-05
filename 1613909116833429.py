l=[]
while(1):
    x=int(input())
    if(x==-1):
        break
    l.append(x)
max_1=max(l)
l.remove(max_1)
max_2=max(l)
print(max_1 , max_2)  

