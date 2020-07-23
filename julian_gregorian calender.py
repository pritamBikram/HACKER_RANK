n=int(input())
def dayOfProgrammer(n):
    if(n<1919 and n!=1918):
        if(n%4==0):
            s1='12'+'.'+'09'+'.'+str(n)
            return s1
        else:
            s2='13'+'.'+'09'+'.'+str(n)
            return s2
    elif(n>=1919):
        if((n%400==0) or (n%4==0 and n%100 !=0)):
            s3='12'+'.'+'09'+'.'+str(n)
            return s3
        else:
            s4='13'+'.'+'09'+'.'+str(n)
            return s4
    elif(n==1918):
        s5='26'+'.'+'09'+'.'+str(n)
        return s5
                                 
print(dayOfProgrammer(n))
            
