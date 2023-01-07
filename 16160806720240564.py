x=input()

def formate_email(email):
    tedade_a=0
    address_a=0
    tedade_dot=0
    address_dot=0
    for i in range(0,len(email)-3):
        if(email[i]=='@' and i>0):
            tedade_a += 1
            address_a=i
    for i in range(0,len(email)-1):
        if(email[i]=='.' and i>address_a ):
            tedade_dot+=1
            address_dot=i
    if(tedade_a==1 and tedade_dot==1):
        for i in range(0,address_a):
            if(email[i] in "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"):
                for i in range(address_a+1,address_dot):
                    if(email[i]=='a' or email[i]=='b'or email[i]=='c' or email[i]=='d' or email[i]=='e' or email[i]=='f'or email[i]=='g' or email[i]=='h' or email[i]=='i' or email[i]=='j'or email[i]=='k' or email[i]=='l' or email[i]=='m' or email[i]=='n'or email[i]=='o' or email[i]=='p' or email[i]=='q' or email[i]=='r'or email[i]=='s' or email[i]=='t' or email[i]=='u' or email[i]=='v'or email[i]=='w' or email[i]=='x' or email[i]=='y' or email[i]=='z' or email[i]=='A' or email[i]=='B'or email[i]=='C' or email[i]=='D' or email[i]=='E' or email[i]=='F'or email[i]=='G' or email[i]=='H' or email[i]=='I' or email[i]=='J'or email[i]=='K' or email[i]=='L' or email[i]=='M' or email[i]=='N'or email[i]=='O' or email[i]=='P' or email[i]=='Q' or email[i]=='R'or email[i]=='S' or email[i]=='T' or email[i]=='U' or email[i]=='V'or email[i]=='W' or email[i]=='X' or email[i]=='Y' or email[i]=='Z'):
                        for i in range(address_dot+1,len(email)):
                            if(email[i]=='a' or email[i]=='b'or email[i]=='c' or email[i]=='d' or email[i]=='e' or email[i]=='f'or email[i]=='g' or email[i]=='h' or email[i]=='i' or email[i]=='j'or email[i]=='k' or email[i]=='l' or email[i]=='m' or email[i]=='n'or email[i]=='o' or email[i]=='p' or email[i]=='q' or email[i]=='r'or email[i]=='s' or email[i]=='t' or email[i]=='u' or email[i]=='v'or email[i]=='w' or email[i]=='x' or email[i]=='y' or email[i]=='z' or email[i]=='A' or email[i]=='B'or email[i]=='C' or email[i]=='D' or email[i]=='E' or email[i]=='F'or email[i]=='G' or email[i]=='H' or email[i]=='I' or email[i]=='J'or email[i]=='K' or email[i]=='L' or email[i]=='M' or email[i]=='N'or email[i]=='O' or email[i]=='P' or email[i]=='Q' or email[i]=='R'or email[i]=='S' or email[i]=='T' or email[i]=='U' or email[i]=='V'or email[i]=='W' or email[i]=='X' or email[i]=='Y' or email[i]=='Z'):
                                return 1

if(formate_email(x)==1):
    print('OK')
else:
    print('WRONG')
