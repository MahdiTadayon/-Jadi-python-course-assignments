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
                    if(email[i] in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"):
                        for i in range(address_dot+1,len(email)):
                            if(email[i] in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"):
                                return 1

if(formate_email(x)==1):
    print('OK')
else:
    print('WRONG')
