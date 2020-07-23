n=input()
s1=n.split()
x1=int(s1[0])
v1=int(s1[1])
x2=int(s1[2])
v2=int(s1[3])

def kangaroo(x1,v1,x2,v2):
    if((x1!=x2 and v1==v2 )or (x2>x1 and v2>v1)):
        s1='NO'
        return s1
    else:
        if(abs(x1-x2)>=abs(v1-v2)):
            rem=abs(x1-x2)/abs(v1-v2)
            print(rem)
            s=str(rem).split(sep='.')
            print(s)
            print(len(s))
            if(len(s)==2):
                if(int(s[1])==0):
                    s21='YES'
                    return s21
                else:
                   s22='NO'
                   return s22
            else:
                s3='NO'
                return s3
        else:
            s4='NO'
            return s4
print(kangaroo(x1,v1,x2,v2))


