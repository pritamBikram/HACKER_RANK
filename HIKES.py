l1=['U','D','D','U']

sea_level=0
m=0
v=0
m_count=0
v_count=0

for i in range(len(l)):
    if(l[i]=='U' and m !=-1):
        m=m+1
        if(m==-1):
            
            v=v-1
        elif(m==0):
            m_count=m_count+1
            
        
    elif(l[i]=='D' and m!=-1):
        m=m-1
        if(m==-1):
            
            v=v-1
        elif(m==0):
            m_count=m_count+1
    elif(l[i]=='D' and v!=1):
        v=v-1
        if(v==1):
            m=1
        elif(v==0):
            v_count=v_count+1
    elif(l[i]=='U' and v!=1):
        v=v+1
        if(v==1):
            m=1
        elif(v==0):
            v_count=v_count+1

print(m_count)
print(v_count)
         
    
    
