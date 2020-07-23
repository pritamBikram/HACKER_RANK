from array import *
keyboards=array('i',[])
drives=array('i',[])
b_n_m=input()
keyboard_element=input()
drive_element=input()
l=b_n_m.split()
b=int(l[0])
l1=keyboard_element.split()
l2=drive_element.split()
for i in l1:
   keyboards.append(int(i))
for j in l2:
    drives.append(int(j))
def getMoneySpent(keyboards,drives,b):
    l=[]
    for i in keyboards:
        for j in drives:
            sum=0
            sum=i+j
            if(sum<=b):
                l.append(sum)
    if(l==[]):
        return -1
    else:
        return (max(l))
print(getMoneySpent(keyboards,drives,b))
          
            
