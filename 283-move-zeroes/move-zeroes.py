class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n=len(nums)
        if n<=1:
            return nums
        j=0
        for i in range(n):
            if nums[i]!=0:
                nums[j],nums[i]=nums[i],nums[j]
                j+=1
        return nums
        