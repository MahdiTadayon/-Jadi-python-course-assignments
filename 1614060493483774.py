n=int(input())
c=dict()
import collections
for i in range(0,n):
    x=input()
    if x in c:
        c[x]+=1
    else: 
        c[x]=1
l=list(c.keys())
len_l=len(l)
min_l=''
for i in range(0,len_l):
    min_l=min(l)
    print(min_l,c[min_l]) 
    l.remove(min(l))        
    
