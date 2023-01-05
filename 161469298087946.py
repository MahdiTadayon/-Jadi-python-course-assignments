def tedade_maghsomon_alai_haye_aval_yek_adad(x):
    c=0
    cc=0
    for i in range(1,x+1):
        if(x%i==0):
            for j in range(1,i+1):
                if(i%j==0):
                    c+=1
        if(c==2):
            cc+=1  
        c=0
    return cc               
t=()
l=[]
for i in range(0,10):
    a=int(input())
    t=(a,tedade_maghsomon_alai_haye_aval_yek_adad(a))
    l.append(t)
l=sorted(l,key=lambda item: (-item[1],-item[0]))    
tt=()
tt=l[0]
print(tt[0],tt[1])