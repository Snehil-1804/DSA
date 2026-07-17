class Solution:
    def lowerBonud(self,nums, target):
        n=len(nums)
        low=0
        high=n-1
        lb=-1
        while low<=high:
            mid=(low+high)>>1
            if nums[mid]>=target:
                lb=mid
                high=mid-1
            else:
                low=mid+1
        return lb
    
    def upperBound(self,nums,target):
        n=len(nums)
        low=0
        high=n-1
        ub=n
        while low<=high:
            mid=(low+high)>>1
            if nums[mid]>target:
                ub=mid
                high=mid-1
            else :
                low=mid+1
        return ub
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l=self.lowerBonud(nums,target)
        if l == -1 or nums[l] != target:
            return [-1, -1]
        r=self.upperBound(nums,target)
        return [l,r-1]
        