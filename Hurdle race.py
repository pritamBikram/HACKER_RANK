from array import *
height=array('i',[])
n_k=input()
jump=input()
l1=n_k.split()
k=int(l1[1])
l2=jump.split()
for i in l2:
    height.append(int(i))
def hurdleRace(k,height):
    maximum=max(height)
    if(k<=maximum):
        j=maximum-k
        return j
    elif(k>maximum):
        return 0
print(hurdleRace(k,height))
