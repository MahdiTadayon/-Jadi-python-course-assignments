iran_win=0
iran_loses=0
iran_draw=0
iran_difference=0
iran_points=0
#
spain_win=0
spain_loses=0
spain_draw=0
spain_difference=0
spain_points=0
#
portugal_win=0
portugal_loses=0
portugal_draw=0
portugal_difference=0
portugal_points=0
#
morocco_win=0
morocco_loses=0
morocco_draw=0
morocco_difference=0
morocco_points=0
#
#
iran_spain=input().split('-')
#print(iran_spain)
if int(iran_spain[0])>int(iran_spain[1]):
    iran_win+=1
    spain_loses+=1
    iran_points+=3
    spain_points+=0
elif int(iran_spain[0])<int(iran_spain[1]):
    spain_win+=1
    iran_loses+=1  
    iran_points+=0
    spain_points+=3 
else:
    iran_draw+=1
    spain_draw+=1
    iran_points+=1
    spain_points+=1  
iran_difference+=int(iran_spain[0])-int(iran_spain[1])
spain_difference+=int(iran_spain[1])-int(iran_spain[0])
#
#
iran_portugal=input().split('-')
if int(iran_portugal[0])>int(iran_portugal[1]):
    iran_win+=1
    portugal_loses+=1
    iran_points+=3
    portugal_points+=0
elif int(iran_portugal[0])<int(iran_portugal[1]):
    portugal_win+=1
    iran_loses+=1  
    iran_points+=0
    portugal_points+=3 
else:
    iran_draw+=1
    portugal_draw+=1
    iran_points+=1
    portugal_points+=1  
iran_difference+=int(iran_portugal[0])-int(iran_portugal[1])
portugal_difference+=int(iran_portugal[1])-int(iran_portugal[0])
#
#
iran_morocco=input().split('-')
if int(iran_morocco[0])>int(iran_morocco[1]):
    iran_win+=1
    morocco_loses+=1
    iran_points+=3
    morocco_points+=0
elif int(iran_morocco[0])<int(iran_morocco[1]):
    morocco_win+=1
    iran_loses+=1  
    iran_points+=0
    morocco_points+=3 
else:
    iran_draw+=1
    morocco_draw+=1
    iran_points+=1
    morocco_points+=1  
iran_difference+=int(iran_morocco[0])-int(iran_morocco[1])
morocco_difference+=int(iran_morocco[1])-int(iran_morocco[0])
#
#
spain_portugal=input().split('-')
if int(spain_portugal[0])>int(spain_portugal[1]):
    spain_win+=1
    portugal_loses+=1
    spain_points+=3
    portugal_points+=0
elif int(spain_portugal[0])<int(spain_portugal[1]):
    portugal_win+=1
    spain_loses+=1  
    spain_points+=0
    portugal_points+=3 
else:
    spain_draw+=1
    portugal_draw+=1
    spain_points+=1
    portugal_points+=1  
spain_difference+=int(spain_portugal[0])-int(spain_portugal[1])
portugal_difference+=int(spain_portugal[1])-int(spain_portugal[0])
#
#
spain_morocco=input().split('-')
if int(spain_morocco[0])>int(spain_morocco[1]):
    spain_win+=1
    morocco_loses+=1
    spain_points+=3
    morocco_points+=0
elif int(spain_morocco[0])<int(spain_morocco[1]):
    morocco_win+=1
    spain_loses+=1  
    spain_points+=0
    morocco_points+=3 
else:
    spain_draw+=1
    morocco_draw+=1
    spain_points+=1
    morocco_points+=1  
spain_difference+=int(spain_morocco[0])-int(spain_morocco[1])
morocco_difference+=int(spain_morocco[1])-int(spain_morocco[0])
#
#
portugal_morocco=input().split('-')
if int(portugal_morocco[0])>int(portugal_morocco[1]):
    portugal_win+=1
    morocco_loses+=1
    portugal_points+=3
    morocco_points+=0
elif int(portugal_morocco[0])<int(portugal_morocco[1]):
    morocco_win+=1
    portugal_loses+=1  
    portugal_points+=0
    morocco_points+=3 
else:
    portugal_draw+=1
    morocco_draw+=1
    portugal_points+=1
    morocco_points+=1  
portugal_difference+=int(portugal_morocco[0])-int(portugal_morocco[1])
morocco_difference+=int(portugal_morocco[1])-int(portugal_morocco[0])
#
#
t_iran=('Iran',iran_win,iran_loses,iran_draw,iran_difference,iran_points)
t_spain=('Spain',spain_win,spain_loses,spain_draw,spain_difference,spain_points)
t_portugal=('Portugal',portugal_win,portugal_loses,portugal_draw,portugal_difference,portugal_points)
t_morocco=('Morocco',morocco_win,morocco_loses,morocco_draw,morocco_difference,morocco_points)
#
#
l=[]
l.append(t_iran)
l.append(t_spain)
l.append(t_portugal)
l.append(t_morocco)
#
#
l=sorted(l,key=lambda item :(-item[5],-item[1],item[0]))
l0=l[0]
l1=l[1]
l2=l[2]
l3=l[3]
print('%s  wins:%i , loses:%i , draws:%i , goal difference:%i , points:%i'   %(l0[0],l0[1],l0[2],l0[3],l0[4],l0[5]))
print('%s  wins:%i , loses:%i , draws:%i , goal difference:%i , points:%i'   %(l1[0],l1[1],l1[2],l1[3],l1[4],l1[5]))
print('%s  wins:%i , loses:%i , draws:%i , goal difference:%i , points:%i'   %(l2[0],l2[1],l2[2],l2[3],l2[4],l2[5]))
print('%s  wins:%i , loses:%i , draws:%i , goal difference:%i , points:%i'   %(l3[0],l3[1],l3[2],l3[3],l3[4],l3[5]))