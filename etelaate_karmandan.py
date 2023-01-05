import mysql.connector
#connecting to db
mydb=mysql.connector.connect(user='root',password='',host='127.0.0.1',database='karmandan')
#connected to db


#
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM table_karmandan")

myresult = mycursor.fetchall()

#for i in myresult:
    #print(i,type(i))
l=[]
for i in myresult:
    l.append(i)
#print(l)
l=sorted(l,key=lambda item : (-item[1],item[2]))
#print(l) 
for i in l:
    print('%s %i %i' %(i[0],i[1],i[2]))