from array import *
number_of_element=input()
element_a=input()
element_b=input()
a=array('i',[])
b=array('i',[])
s1=element_a.split()
for i in s1:
    a.append(int(i))
s2=element_b.split()
for i in s2:
    b.append(int(i))
def getTotalX(a,b):
    n=max(b)
    l4=[]
    for i in range(1,n+1):
        p1=[]
        for j in b:
            f1=0
            if(j%i==0):
                f1=1
                p1.append(f1)
            else:
                p1.append(f1)
        
        flag1=0
        for k in p1:
            if(k==0):
                flag1=1
        if(flag1==0):
          l4.append(i)
        
    #print(l4)
    # SECOND_PART
    fi=[]
    for l in l4:
        p=[]
        for m in a:
            f=0
            if(l%m==0):
                f=1
                p.append(f)
            else:
                p.append(f)
        
        flag=0
        for x in p:
            if(x==0):
                flag=1
        if(flag==0):
          fi.append(l)
    a=len(fi)
    return a
print(getTotalX(a,b))
