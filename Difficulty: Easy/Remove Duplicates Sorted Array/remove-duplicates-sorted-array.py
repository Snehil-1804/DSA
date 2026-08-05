class Solution:
    def removeDuplicates(self, arr):
        n=len(arr)
        ans=[]
        for i in range(n):
            if i==0:
                ans.append(arr[i])
            elif arr[i]!=arr[i-1]:
                ans.append(arr[i])
        return ans