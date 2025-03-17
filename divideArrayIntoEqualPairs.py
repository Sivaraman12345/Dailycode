nums=list(map(int,input().split()))
seen={}
for i in nums:
    seen[i]=seen.get(i,0)+1
p=0
for i in seen:
    if seen[i]%2!=0:
        print("Not Possible")
        p=1
        break
if not p:
    print("Possible")
# space complexity: O(n)
# time complexity: O(n)
