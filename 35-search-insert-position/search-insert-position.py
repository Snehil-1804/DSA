class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n=len(nums)
        low=0
        high=n-1
        position=n
        while low<=high:
            mid=(low+high)>>1
            if nums[mid]>=target:
                position=mid
                high=mid-1
            else:
                low=mid+1
        return position
        