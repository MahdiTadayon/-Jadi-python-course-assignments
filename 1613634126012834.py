x = input()
x = int(x)
i = 2
c = 0
while(x != i):
    if(x % i != 0):
        c += 1
    i += 1

if(x-2 == c):
    print('prime')
else:
    print('not prime')