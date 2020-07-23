q=int(input())
l=[]
for i in range(q):
    x=input()
    l.append(x)
def catAndMouse(x,y,z):
    cata=abs(z-x)
    catb=abs(z-y)
    if(cata<catb):
        return 'Cat A'
    elif(catb<cata):
        return 'Cat B'
    elif(cata==catb):
        return 'Mouse C'
for i in l:
    a=i.split()
    x=int(a[0])
    y=int(a[1])
    z=int(a[2])
    print(catAndMouse(x,y,z))

