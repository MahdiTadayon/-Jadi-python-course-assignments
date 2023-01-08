x=input().lower()
y=''
for i in range(0,len(x)):
    if not x[i] in 'aeiou' :
        y=y+'.'+x[i]

print(y)
        
