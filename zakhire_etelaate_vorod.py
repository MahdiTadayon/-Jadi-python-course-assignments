import mysql.connector
#connecting to db
mydb=mysql.connector.connect(user='root',password='',host='127.0.0.1',database='etelaat')
#connected to db


#
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM table_etelaat")

myresult = mycursor.fetchall()
#formate email
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
            if(email[i]=='1' or email[i]=='2'  or email[i]=='3' or email[i]=='4' or email[i]=='5' or email[i]=='6'or email[i]=='7' or email[i]=='8' or email[i]=='9'or email[i]=='0'  or email[i]=='a' or email[i]=='b'or email[i]=='c' or email[i]=='d' or email[i]=='e' or email[i]=='f'or email[i]=='g' or email[i]=='h' or email[i]=='i' or email[i]=='j'or email[i]=='k' or email[i]=='l' or email[i]=='m' or email[i]=='n'or email[i]=='o' or email[i]=='p' or email[i]=='q' or email[i]=='r'or email[i]=='s' or email[i]=='t' or email[i]=='u' or email[i]=='v'or email[i]=='w' or email[i]=='x' or email[i]=='y' or email[i]=='z' or email[i]=='A' or email[i]=='B'or email[i]=='C' or email[i]=='D' or email[i]=='E' or email[i]=='F'or email[i]=='G' or email[i]=='H' or email[i]=='I' or email[i]=='J'or email[i]=='K' or email[i]=='L' or email[i]=='M' or email[i]=='N'or email[i]=='O' or email[i]=='P' or email[i]=='Q' or email[i]=='R'or email[i]=='S' or email[i]=='T' or email[i]=='U' or email[i]=='V'or email[i]=='W' or email[i]=='X' or email[i]=='Y' or email[i]=='Z' ):
                for i in range(address_a+1,address_dot):
                    if(email[i]=='a' or email[i]=='b'or email[i]=='c' or email[i]=='d' or email[i]=='e' or email[i]=='f'or email[i]=='g' or email[i]=='h' or email[i]=='i' or email[i]=='j'or email[i]=='k' or email[i]=='l' or email[i]=='m' or email[i]=='n'or email[i]=='o' or email[i]=='p' or email[i]=='q' or email[i]=='r'or email[i]=='s' or email[i]=='t' or email[i]=='u' or email[i]=='v'or email[i]=='w' or email[i]=='x' or email[i]=='y' or email[i]=='z' or email[i]=='A' or email[i]=='B'or email[i]=='C' or email[i]=='D' or email[i]=='E' or email[i]=='F'or email[i]=='G' or email[i]=='H' or email[i]=='I' or email[i]=='J'or email[i]=='K' or email[i]=='L' or email[i]=='M' or email[i]=='N'or email[i]=='O' or email[i]=='P' or email[i]=='Q' or email[i]=='R'or email[i]=='S' or email[i]=='T' or email[i]=='U' or email[i]=='V'or email[i]=='W' or email[i]=='X' or email[i]=='Y' or email[i]=='Z'):
                        for i in range(address_dot+1,len(email)):
                            if(email[i]=='a' or email[i]=='b'or email[i]=='c' or email[i]=='d' or email[i]=='e' or email[i]=='f'or email[i]=='g' or email[i]=='h' or email[i]=='i' or email[i]=='j'or email[i]=='k' or email[i]=='l' or email[i]=='m' or email[i]=='n'or email[i]=='o' or email[i]=='p' or email[i]=='q' or email[i]=='r'or email[i]=='s' or email[i]=='t' or email[i]=='u' or email[i]=='v'or email[i]=='w' or email[i]=='x' or email[i]=='y' or email[i]=='z' or email[i]=='A' or email[i]=='B'or email[i]=='C' or email[i]=='D' or email[i]=='E' or email[i]=='F'or email[i]=='G' or email[i]=='H' or email[i]=='I' or email[i]=='J'or email[i]=='K' or email[i]=='L' or email[i]=='M' or email[i]=='N'or email[i]=='O' or email[i]=='P' or email[i]=='Q' or email[i]=='R'or email[i]=='S' or email[i]=='T' or email[i]=='U' or email[i]=='V'or email[i]=='W' or email[i]=='X' or email[i]=='Y' or email[i]=='Z'):
                                return 1
               


#for i in myresult:
    #print(i)




#if(formate_email=='hasan@yahoo.com'):
    #print('yes')



#for i in myresult:
    #if(formate_email(i)==1):
       


mydb2=mysql.connector.connect(user='root',password='',host='127.0.0.1',database='etelaat2')
mycursor2 = mydb2.cursor()
mycursor2.execute("CREATE TABLE table_etelaat4 ( name VARCHAR(255), password VARCHAR(255))")
sql = "INSERT INTO table_etelaat4 (name, password) VALUES (%s, %s)"
#val = ("John", "Highway 21")
#mycursor2.execute(sql, val)

#mydb2.commit()



for i in myresult:
    if(formate_email(i[0])==1):
        sql = "INSERT INTO table_etelaat4 (name, password) VALUES (%s, %s)"
        val = (i[0], i[1])
        mycursor2.execute(sql, val)
        mydb2.commit()
    else:
        while(1):
            print('expression@string.string')
            u=input()
            #p=input()
            if(formate_email(u)==1):
                sql = "INSERT INTO table_etelaat4 (name, password) VALUES (%s, %s)"
                val = (u, i[1])
                mycursor2.execute(sql, val)
                mydb2.commit()
                break


