n=input()
def timeConversion(n):
    for i in n:
        if(i=='P'):
            m=n.split(sep=':')
            
            z=m[2].split('PM')
            m[2]=z[0]
            
            l=[]
            for i in m:
                l.append(int(i))
            
            if(l[0]==12):
                s1=str(l[0])+':'+m[1]+':'+m[2]
            else:
                l[0]=l[0]+12
                s1=str(l[0])+':'+m[1]+':'+m[2]
            
            
        elif(i=='A'):
            m=n.split(sep=':')
            
            z=m[2].split('AM')
            m[2]=z[0]
            
            l=[]
            for i in m:
                l.append(int(i))
            
            if(l[0]==12):
                
                s1='00'+':'+m[1]+':'+m[2]
            else:
                s1=str(l[0])+':'+m[1]+':'+m[2]
                
            
    return s1

print(timeConversion(n))
    

