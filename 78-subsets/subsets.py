class Solution:
    def solve(self,i,nums,subset,res):
        if i>=len(nums):
            res.append(subset.copy())
            return res
        subset.append(nums[i])
        self.solve(i+1,nums,subset,res)
        subset.pop()
        self.solve(i+1,nums,subset,res)

    def subsets(self, nums: list[int]) -> list[list[int]]:
        res=[]
        subset=[]
        self.solve(0,nums,subset,res)
        return res
