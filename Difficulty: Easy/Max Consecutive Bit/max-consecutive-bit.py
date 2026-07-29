class Solution:
    def maxConsecBits(self, arr):
        #code here 
        n=len(arr)
        count=1
        max_count=1
        
        for i in range(1,n):
            if arr[i]==arr[i-1]:
                count+=1
            else:
                count=1
            max_count=max(max_count,count)
        return max_count