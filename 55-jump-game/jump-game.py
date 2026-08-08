class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        maxjumps=0
        for i in range(n):
            if i>maxjumps:
                return False
            maxjumps=max(maxjumps,i+nums[i])
        return True 
        