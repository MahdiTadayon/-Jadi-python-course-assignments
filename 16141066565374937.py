n=int(input())
import math
l=[]

for i in range(0,n):
    x=int(input())
    
    rishe=math.sqrt(x)
    m=rishe
    c=0
    rishe=float(rishe)
    rishe=str(rishe)
    
    rishe=rishe+'000'
    
    m=int(m)
    
    while(m!=0):
        m=m//10
        c+=1

    r=''
    r=rishe[:c+5]
    
    l.append(r)    
for i in range(0,n):
    print(l[i])






    





        
