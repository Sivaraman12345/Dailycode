class Solution(object):
    def minOperations(self, nums):
        ctr=0
        for i in range(len(nums)-2):
            
            if nums[i]!=1:
                nums[i],nums[i+1],nums[i+2]= nums[i]^1,nums[i+1]^1,nums[i+2]^1
                ctr+=1
        return ctr if nums[-1]==1 and nums[-2]==1 else -1
