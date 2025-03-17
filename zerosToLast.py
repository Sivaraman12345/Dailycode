lis=list(map(int,input().split()))
n=len(lis)
for i in range(n):
    if lis[i]==0:
        lis.append(lis.pop(i))
print(lis)