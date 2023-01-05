x=input()
x=x.split()
max=0
a=int(x.pop())
b=int(x.pop())
c=int(x.pop())
if(a>=b and a>=c):
    max=a
elif(b>=a and b>=c): 
    max=b
else:
    max=c
if(a<=b and a<=c):
    min=a
elif(b<=a and b<=c):
    min=b
else:
    min=c
print(max-min)
                       


