class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n=len(nums)
        count=0
        maxcount=0
        for i in range(0,n):
            if nums[i]==1:
                count+=1
                maxcount=max(count,maxcount)
            else:
                count=0
        return maxcount