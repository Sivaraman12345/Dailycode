from typing import List

class Solution:
    def uniqueNumber(self,nums:List[int])->int: 
        unique=0
        for i in nums:
            unique^=i
        return unique
lis=list(map(int,input().split()))
print(Solution().uniqueNumber(lis))
# Time Complexity: O(n)
# Space Complexity: O(1)