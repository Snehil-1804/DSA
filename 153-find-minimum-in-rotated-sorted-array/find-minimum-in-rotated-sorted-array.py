class Solution:
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)
        low=0
        high=n-1
        mini=float("inf")
        while low<=high:
            mid=(low+high)//2
            if nums[mid]<=nums[high]:
                mini=min(mini,nums[mid])
                high=mid-1
                
            else:
                mini=min(mini,nums[mid])
                low=mid+1
        return mini
