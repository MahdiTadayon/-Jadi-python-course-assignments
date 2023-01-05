n=int(input())
Horror=0
Romance=0 
Comedy=0
History=0
Adventure=0
Action=0
l=[]
for i in range(0,n):
    x=input().split()
    if 'Horror' in x:
        Horror+=1
    if 'Romance' in x:
        Romance+=1
    if 'Comedy' in x:
        Comedy+=1
    if 'History' in x:
        History +=1     
    if 'Adventure' in x:
        Adventure+=1
    if 'Action' in x:
        Action+=1
    x=[]    
t=(Horror,'Horror') 
l.append(t)
t=(Romance,'Romance') 
l.append(t)
t=(Comedy,'Comedy') 
l.append(t)
t=(History,'History') 
l.append(t)
t=(Adventure,'Adventure') 
l.append(t)
t=(Action,'Action') 
l.append(t)
#print(l)
l=sorted(l,key=lambda item :(-item[0],item[1]))
#print(l)
for i in l:
    print('%s : %i' %(i[1],i[0]))