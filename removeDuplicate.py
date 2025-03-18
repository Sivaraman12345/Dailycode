# Remove duplicates from a string
s=input().strip()
seen=set()
s1=''
for i in s:
    if i not in seen:
        s1+=i
        seen.add(i)
print(s1)