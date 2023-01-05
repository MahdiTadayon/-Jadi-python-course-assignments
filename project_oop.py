import random
class Ensan:
    
    def __init__(self,name):
        self.name=name
        
    def f(self):
        l=[]
        l=self.name
        A=[]
        B=[]
        i=0
        j=0
        while(i!=11):
            random.shuffle(l)
            A.append(l.pop())
            i+=1
        while(j!=11):    
            random.shuffle(l)
            B.append(l.pop())
            j+=1
        for i in range(0,11):
            print(A[i]+' '+'A')
        for i in range(0,11):
            print(B[i]+' '+'B')
class Footballist(Ensan):
    pass

l1=Footballist(['reza','ali','behroz','mohsen','shahroz','saman',
'behzad','soheil','hossein','maziar','akbar','nima','mahdi','farhad',
'mohammad','khashayar','milad','mostafa','amin','saeid','pooya','poorya'])
#
"""p1=Footballist('hossein')
p2=Footballist('maziar')
p3=Footballist('akbar')
p4=Footballist('nima')
p5=Footballist('mahdi')
p6=Footballist('farhad')
p7=Footballist('mohammad')
p8=Footballist('khashayar')
p9=Footballist('milad')
p10=Footballist('mostafa')
p11=Footballist('amin')
p12=Footballist('saeid')
p13=Footballist('pooya')
p14=Footballist('poorya')
p15=Footballist('reza')
p16=Footballist('ali')
p17=Footballist('behzad')
p18=Footballist('soheil')
p19=Footballist('behroz')
p20=Footballist('shahroz')
p21=Footballist('saman')
p22=Footballist('mohsen')"""
#
#
#
l1.f()
