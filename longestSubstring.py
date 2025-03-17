while True:
    a=input().strip()
    n=len(a)
    maxlen=0
    left=0
    chars=set()
    for right in range(n):
        while a[right] in chars:
            chars.remove(a[left])
            left+=1
        chars.add(a[right])
        maxlen=max(maxlen,right-left+1)
    print(maxlen)
# Time Complexity: O(n)
# Space Complexity: O(n)
