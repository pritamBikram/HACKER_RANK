from array import *
arr=array('i',[])
n=int(input())
for i in range(n):
    x=int(input())
    arr.append(x)

def gradingStudents(arr):
    l=[]
    for i in range(len(arr)):
        if(arr[i]>=38):
            div=arr[i]//5
            new_div=div+1
            new_num=new_div*5
            if(new_num-arr[i]<3):
                l.append(new_num)
            else:
                l.append(arr[i])
            
        else:
            l.append(arr[i])
    return l
k=gradingStudents(arr)
for i in k:
    print(i)
