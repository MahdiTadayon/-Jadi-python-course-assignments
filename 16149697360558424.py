from re import search
x=input().split()
x.append('0')
x.append('0')
#
for j in x:
    for i in range(0,len(x)-1):
        s=''
        s=s+x[i]
        if(s[-1]=='.'):
            x[i+1]='0'
            
#print(x)
#print(x)
#def tashkhise_kalamate_shakhes:
c=0
for i in range(1,len(x)):
    if '.' in x[i]:
        x[i]=x[i].replace('.','')
        
    if ',' in x[i]:
        x[i]=x[i].replace(',','')    

    if(x[i]<x[i].lower()):
        c+=1
        print('%i:%s' %(i+1,x[i]))
if(c==0):
    print('None')
#print(x)

