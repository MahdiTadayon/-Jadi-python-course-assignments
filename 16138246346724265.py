x=int(input())
y=input().split()
w=[]
for i in range(0,x):
    a=int(y.pop())
    w.append(a)
q=[]
for i in range(0,x):
    if(w[i]<3):
        q.append(w[i])

print(len(q)//3)


