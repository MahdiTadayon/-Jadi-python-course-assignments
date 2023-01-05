import hashlib
import csv
def hash_password_hack(input_file_name, output_file_name):
    my_dict=dict()
    for i in range(1000,10000):
        i=str(i)
        r=hashlib.sha256(i.encode()).hexdigest()
        my_dict[i]=r
        r=''
#print(my_dict)
    f=open(input_file_name,'r')  
    reader=csv.reader(f)
    for row in reader:
    #print(row)
        for i in range(1000,10000):
            i=str(i)
            if(row[1]==my_dict[i]):
            #print(my_dict)
                print(row[0],i)
            #print(type(row[0]),type(i))
                with open(output_file_name,'a') as final:
            
                    final.write('%s,%s\n' %(row[0],i))
                