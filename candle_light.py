from array import *
n=int(input())
candle_height=input()
l=candle_height.split()
arr=array('i',[])
for i in l:
    arr.append(int(i))
def birthdayCakeCandles(arr):
    maximum=max(arr)
    count=0
    for i in range(len(arr)):
        if(arr[i]==maximum):
            count=count+1
    return count
print(birthdayCakeCandles(arr))
