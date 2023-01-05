import random
l=[]
l2=[]
i=0
for i in range(1,100):
    l.append(i)
a=min(l)
b=max(l)
hads=random.randint(a,b)
print(hads)
man=input()
i=0
while(1):
    
    if(man=='k'):
        c=0
        i=0
        for i in range(0,99):
            if(hads<=l[i]):
                l.remove(l[i])
                c+=1
                l.append(0)
                l.sort()
        while(len(l)!=99):
            l.append(0)
            l.sort()     
            
        for j in range(0,99):
            if(l[0]==0):
                l.remove(l[0]) 
               
        a=min(l)
        b=max(l) 
        while(len(l)!=99):
            l.append(0)
            l.sort()   
               
        hads=random.randint(a,b)
        print(hads)
        man=input()
        i=0
        
    elif(man=='b'):
        cc=0
        i=0
        while(hads>=l[i]):
            l.remove(l[i])
            cc+=1
            l.append(0)
            l.sort()
            i+=1
        while(len(l)!=99):
            l.append(0)
            l.sort()   
       
        for j in range(0,99):
            if(l[0]==0):
                l.remove(l[0])  
          
        a=min(l)
        b=max(l)   
        while(len(l)!=99):
            l.append(0)
            l.sort()   
             
        hads=random.randint(a,b)
        print(hads)
        man=input()
        i=0
    elif(man=='d'):
        break
       
