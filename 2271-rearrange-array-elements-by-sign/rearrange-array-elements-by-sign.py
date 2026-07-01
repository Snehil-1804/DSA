class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        pos=0
        neg=1
        result=[]
        for i in range(n):
            if nums[i]>=0:
                result.insert(pos,nums[i])
                pos+=2
            else:
                result.insert(neg,nums[i])
                neg+=2
        return result
        