lis=list(map(int,input().split()))
n=len(lis)
seen = {}

for i in lis:
    if i in seen:
        seen[i] += 1
    else:
        seen[i] = 1

for i in lis:
    if seen[i] == 1:
        print(i)
        break
