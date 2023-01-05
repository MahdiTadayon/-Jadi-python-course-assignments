x=input()
c=0
for i in range(0,len(x)):
    if(x[i]=='h'):
        c+=1
        x=x[i+1:]
        break
for i in range(0,len(x)):
    if(x[i]=='e'):
        c+=1
        x=x[i+1:]
        break
for i in range(0,len(x)):
    if(x[i]=='l'):
        c+=1
        x=x[i+1:] 
        break
for i in range(0,len(x)):
    if(x[i]=='l'):
        c+=1
        x=x[i+1:]
        break
for i in range(0,len(x)):
    if(x[i]=='o'):
        c+=1
        x=x[i+1:]
        break
if(c==5):
    print('YES')
else:
    print('NO')
                           
