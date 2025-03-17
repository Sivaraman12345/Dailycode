n=list(map(int,input().split()))
n.sort()
total=0
for i in  range(len(n)):
    j,k=0,i-1
    while j<k:
        if n[j]+n[k]==n[i]:
            total+=1
            j+=1
            k-=1
        elif n[j]+n[k]<n[i]:
            j+=1
        else:
            k-=1
print(total)