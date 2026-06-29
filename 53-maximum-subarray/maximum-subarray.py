class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        maxi=float("-inf")
        total=0
        for i in range(n):
            total+=nums[i]
            maxi=max(maxi,total)
            if total<0:
                total=0
        return maxi