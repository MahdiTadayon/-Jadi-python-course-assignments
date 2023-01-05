x=input()
y=''
for i in range(0,len(x)):
    if(x[i]=='1'):
        y=y+'1+'
for i in range(0,len(x)):
    if(x[i]=='2'):
        y=y+'2+'
for i in range(0,len(x)):
    if(x[i]=='3'):
        y=y+'3+'
y=y[0:-1] 
print(y)       

