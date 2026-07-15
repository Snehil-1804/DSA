class Solution:
    def findTwoElement(self, arr):
        # code here
        n=len(arr)
        ans = [0]*(n+1)
        
        for i in range(n):
            ans[arr[i]]+=1
            
        double=0
        missing=0
        
        for i in range(0,n+1):
            if ans[i]==2:
                double=i
            elif ans[i]==0:
                missing=i
        return[double,missing]
