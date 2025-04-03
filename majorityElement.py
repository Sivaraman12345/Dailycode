import math
lis=list(map(int, input().split()))
n=len(lis)
N=math.floor(n/2)
for i in lis:
    if lis.count(i)>N:
        print(i,end=' ')
        break