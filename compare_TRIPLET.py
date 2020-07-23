x=input()
y=input()

a=x.split()
b=y.split()

a=[int(i) for i in a]
b=[int(i) for i in b]

def compareTriplets(a,b):
    a1=0
    b1=0
    i=len(a)
    reward=[]
    while(i>0):
        if(a[i-1]>b[i-1]):
            a1=a1+1
        elif(a[i-1]<b[i-1]):
            b1=b1+1
        i=i-1
    s1=str(a1)
    s2=str(b1)
    reward.append(s1)
    reward.append(s2)
    c=' '.join(reward)
    return c


print(compareTriplets(a,b))
    
