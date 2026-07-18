class Solution:
    def lowerBound(self,arr,target):
        n=len(arr)
        low=0
        high=n-1
        lb=-1
        while low<=high:
            mid=(low+high)//2
            
            if arr[mid]>=target:
                lb=mid
                high=mid-1
            else:
                low=mid+1
        return lb
    def upperBound(self,arr,target):
        n=len(arr)
        low=0
        high=n-1
        ub=n
        while low<=high:
            mid=(low+high)//2
            
            if arr[mid]>target:
                ub=mid
                high =mid-1
            else:
                low=mid+1
        return ub
    def countFreq(self, arr, target):
        # code here
        lb=self.lowerBound(arr,target)
        if lb == -1 or arr[lb] != target:
            return 0
        ub= self.upperBound(arr,target)
        return ub-lb