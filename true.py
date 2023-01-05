import requests
import re
from bs4 import BeautifulSoup
import mysql.connector
c=0
s=""
w=0
v=0

r=requests.get('https://www.carnext.com/en-de/cars/volkswagen/')
soup=BeautifulSoup(r.text,'html.parser')
KMs=soup.find_all("p" ,class_="Label-sc-1xzhlt8-0 epjYiC")
while(v!=19):
    for j in KMs:
    
        for k in j.text:
            
            if(k == "|"):
                c = c+1
            if(c == 4):
                s = s+k
        c = 0
        s = s+" "
        v=v+1
ss = ""    


l1=s.split()
for i in l1:
    if(i=="|"):
        l1.remove("|")
        l1.remove("km")



l2=[]
prices=soup.find_all("span", attrs={"data-e2e-id":"viewerBuyPrice"})
while(w!=19):
    for i in prices:
        l2.append(i.text)
        w=w+1
    

mydb=mysql.connector.connect(user='root',password='',host='127.0.0.1')
mycursor=mydb.cursor()
mycursor.execute("CREATE DATABASE car")
mycursor.execute("CREATE TABLE price_kms (price VARCHAR(255), kms VARCHAR(255))")
sql="INSERT INTO car (price,kms) VALUES (%s ,%s) "
for i in range(0,len(l1)) :
    val=(l1[i],l2[i])
    mycursor.execute(sql,val)
    mydb.commit()
