class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n=len(nums)
        ans=[]
        nums.sort()
        my_set=set()
        for i in range(n):
            if nums[i]!=0 and nums[i]==nums[i-1]:
                continue
            j=i+1
            k=n-1
            while j<k:
                total_sum=nums[i]+nums[j]+nums[k]
                if total_sum>0:
                    k-=1
                elif total_sum<0:
                    j+=1
                else:
                    temp=[nums[i],nums[j],nums[k]]
                    my_set.add(tuple(temp))
                    j+=1
                    k-=1
                    while j<k and nums[j]==nums[j-1]:
                        j+=1
                    while j<k and nums[k]== nums[k+1]:
                        k-=1
        return [list(ans) for ans in my_set]