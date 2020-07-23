from array import *
n_k=input()
element=input()
l=n_k.split()
n=int(l[0])
k=int(l[1])
ar=array('i',[])
k1=element.split()
for i in k1:
    ar.append(int(i))
def divisibleSumPairs(n,ar,k):
    count=0
    for i in range(n):
        for j in range(i+1,n):
            sum=0
            sum=sum+ar[i]+ar[j]
            if(sum%k==0):
                count=count+1
    return count
print(divisibleSumPairs(n,ar,k))
                
