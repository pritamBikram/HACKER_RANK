from array import *
n=int(input())
s=input()
score=array('i',[])
l=s.split()
for i in l:
    score.append(int(i))
def breakingRecords(score):
    max_score=score[0]
    min_score=score[0]
    max_count=0
    min_count=0
    for i in score:
        if(i<min_score):
            min_score=i
            min_count=min_count+1
        elif(i>max_score):
            max_score=i
            max_count=max_count+1
    c=' '.join([str(max_count),str(min_count)])
    return c
print(breakingRecords(score))
