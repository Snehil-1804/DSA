class Solution:
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)
        low=0
        high=n-1
        while low<high:
            mid=(low+high)//2
            if nums[mid]<=nums[high]:
                high=mid
            else:
                low=mid+1
        return nums[low]
