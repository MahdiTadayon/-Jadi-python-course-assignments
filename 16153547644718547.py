
import datetime

class Sen:
    
    def __init__(self,date):
        self.date=date
        
    def f(self):
        y=self.date
        if(len(y)!=10 or y[5:7]>'12' or y[8:10]>'31' or y[4]!='/' or y[7]!='/'):
            print('WRONG')
            return 0


        sale_tavalod=int(y[0:4])  
        mahe_tavalod=int(y[5:7])
        roze_tavalod=int(y[8:10])
        #
        '''print(sale_tavalod)
        print(mahe_tavalod)
        print(roze_tavalod)'''
        x=''
        x=str(datetime.datetime.now())
        #print(x)
        sale_kononi=int(x[0:4])
        mahe_kononi=int(x[5:7])
        roze_kononi=int(x[8:10])
        #
        '''print(sale_kononi)
        print(mahe_kononi)
        print(roze_kononi)'''
        
        #print(x)
        #x=int(x)
        #if(len(y)==10 and int(y[5:7])<32 and int(y[8:10])<13 and y[4]=='/' and y[7]=='/'):
        if(mahe_tavalod>mahe_kononi):
            print(sale_kononi-sale_tavalod-1)
        elif(mahe_tavalod<mahe_kononi):
            print(sale_kononi-sale_tavalod)
        elif(mahe_tavalod==mahe_kononi):
            if(roze_tavalod>roze_kononi):
                print(sale_kononi-sale_tavalod-1)
            else:
                print(sale_kononi-sale_tavalod) 
        
d1=Sen(input())
d1.f()



