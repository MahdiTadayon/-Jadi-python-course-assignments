x=input()
c=0
for i in range(0,len(x)):
    if(x[i]<'a'):
	    c+=1
if(c>len(x)-c):
	x=x.upper()
	print(x)
else:
    x=x.lower()
    print(x)
