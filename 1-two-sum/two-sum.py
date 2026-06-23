class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        freq={}
        for i in range(0,n):
            remaining=target-nums[i]
            if remaining in freq:
                return [freq.get(remaining),i] 
            else:
                freq[nums[i]]=i
        