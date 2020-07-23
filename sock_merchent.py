from array import *
n=int(input())
socks=input()
ar=array('i',[])
l=socks.split()
for i in l:
    ar.append(int(i))

def sockMerchant(n,ar):
    l=[]
    c=[]
    for i in range(n):
        flag=0
        
        for k in range(len(l)):
            if(l[k]==ar[i]):
                flag=1
                break;
        
        if(flag==0):
            l.append(ar[i])
            count=0
            for j in range(i,n):
                if(ar[j]==ar[i]):
                    count=count+1
            c.append(count)
    pair=0
    for ii in c:
        pair=pair+ii//2
    return pair
print(sockMerchant(n,ar))

                
        
