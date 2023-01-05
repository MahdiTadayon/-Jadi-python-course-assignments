x=input().lower()
c=0
for i in range(0,len(x)):
    if(x[i]==x[len(x)-1-i]):
        c+=1
if(c>=len(x)/2):
    print('palindrome')
else:
    print('not palindrome')  
