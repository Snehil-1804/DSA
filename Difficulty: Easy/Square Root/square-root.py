class Solution:
    def floorSqrt(self, n): 
        # code here
        if n==0 or n==1:
            return n
        low=0
        high=n
        ans=0
        while low<=high:
            mid=(low+high)//2
            if mid*mid==n:
                return mid
            elif mid*mid<n:
                ans=mid
                low=mid+1
            else:
                high=mid-1
        return ans
        