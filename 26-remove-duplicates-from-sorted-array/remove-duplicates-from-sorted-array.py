class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return 1
        i=0
        j=i+1
        while j<n:
            if nums[j]!=nums[i]:
                i+=1
                nums[i],nums[j]=nums[j],nums[i]
            j+=1
        return i+1
        # freq_map={}
        # for i in range(0,n):
        #     freq_map[nums[i]]=0
        # j=0
        # for k in freq_map:
        #     nums[j]=k
        #     j+=1
        # return j
