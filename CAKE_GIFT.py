from array import *
n=int(input())
choclate=input()
d_m=input()
l=choclate.split()
s=array('i',[])
for i in l:
    s.append(int(i))
h=d_m.split()
d=int(h[0])
m=int(h[1])
def birthday(s,d,m):
    count=0
    for i in range(len(s)):
        if(i+m<=len(s)):
            sum=0
            for j in range(i,i+m):
                sum=sum+s[j]
            if(sum==d):
                count=count+1
    return count
print(birthday(s,d,m))
                   
