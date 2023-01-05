
class Madrase:
    def __init__(self,age,height,weight):
        self.age=age.split()

        self.height=height.split()
    
        self.weight=weight.split()
       
    def myfunc(self):
        
        intage = [int(item) for item in self.age]
        intheight = [int(item) for item in self.height] 
        intweight = [int(item) for item in self.weight] 

        print(float(sum(intage)/len(intage)))
        print(float(sum(intheight)/len(intheight)))
        print(float(sum(intweight)/len(intweight)))
    def f_A_B(self):
        intheight = [int(item) for item in self.height] 
        x=float(sum(intheight)/len(intheight))
        return x
    def fAB(self):
        intweight = [int(item) for item in self.weight]
        y=float(sum(intweight)/len(intweight))
        return y




n=int(input())
madraseA=Madrase(input(),input(),input())

m=int(input())
madraseB=Madrase(input(),input(),input())

madraseA.myfunc()
madraseB.myfunc()
#print(madraseA.age)
#
'''print(madraseA.f_A_B())
print(madraseB.f_A_B())
print(madraseA.fAB())
print(madraseB.fAB())'''


#
if(madraseA.f_A_B()>madraseB.f_A_B()):
    print('A')
elif(madraseA.f_A_B()<madraseB.f_A_B()):
    print('B')
elif(madraseA.f_A_B()==madraseB.f_A_B()):
    if(madraseA.fAB()>madraseB.fAB()):
        print('A')    
    elif(madraseA.fAB()<madraseB.fAB()):
        print('B')   
    else:
        print('Same')    
