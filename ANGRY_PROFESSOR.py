t=int(input())
l=[]
l1=[]
for i in range(t):
    x=input()
    y=input()
    l.append(x)
    l1.append(y)

def angryProfessor(k,a):
    count=0
    for i in range(len(a)):
        if(a[i]<=0):
            count=count+1
    print(k)
    
    if(count>=k):
        return 'NO'
    else:
        return 'YES'
for i in range(len(l)):
    h=l[i].split()
    k=int(h[1])
    c=l1[i].split()
    a=[int(d) for d in c]
    print(angryProfessor(k,a))
