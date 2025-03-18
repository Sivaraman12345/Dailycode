class Solution(object):
    def longestNiceSubarray(self, nums):
        left=0
        maxlength=0
        bitmask=0
        for right in range(len(nums)):
            while bitmask&nums[right]!=0:
                bitmask^=nums[left]
                left+=1
            bitmask|=nums[right]
            maxlength=max(maxlength,right-left+1)
        return maxlength
        