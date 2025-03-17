lis=list(map(int,input().split()))
k=int(input())
print(lis[-k:]+lis[:-k])