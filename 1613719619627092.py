x=input().lower()
y=''
for i in range(0,len(x)):
    if(x[i]!='a' and x[i]!='e' and  x[i]!='i' and x[i]!='o' and x[i]!='u'):
        y=y+'.'+x[i]

print(y)
        
