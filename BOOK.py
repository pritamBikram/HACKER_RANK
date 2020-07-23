n=int(input())
p=int(input())
def pageCount(n,p):
    if(n%2==0):
        # from first
        if(p==1):
            count=0
        else:
            count=0
            page_no=1
            while(page_no<=n):
                count=count+1
                if(((page_no+1)==p) or ((page_no+2)==p)):
                    break
                page_no=page_no+2
        #from last
        if(p==n):
            c1=0
        else:
            p1=n
            c1=0
            while(p1>=1):
                c1=c1+1
                if(((p1-1)==p) or ((p1-2)==p)):
                    break
                p1=p1-2
    else:
        # from first
        if(p==1):
            count=0
        else:
            count=0
            page_no=1
            while(page_no<=n):
                count=count+1
                if(((page_no+1)==p) or ((page_no+2)==p)):
                    break
                page_no=page_no+2
        #from last
        p1=n+1
        c1=0
        while(p1>=1):
            
            if(((p1-1)==p) or ((p1-2)==p)):
                break
            c1=c1+1
            p1=p1-2
    minimum=0
    if(count<c1):
        minimum=count
    else:
        minimum=c1
    return minimum
print(pageCount(n,p))
        
