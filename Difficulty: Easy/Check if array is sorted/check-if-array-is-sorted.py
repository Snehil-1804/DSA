class Solution:
    def isSorted(self, arr) -> bool:
        # code here
        n=len(arr)
        for i in range(0,n-1):
            if arr[i]>arr[i+1]:
                return False
        return True