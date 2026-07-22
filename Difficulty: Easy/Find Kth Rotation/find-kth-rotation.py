class Solution:
    def findKRotation(self, arr):
        # code here
        l= 0
        h = len(arr)-1
        while(l<h):
            m = (l+h)//2
            if arr[m]>arr[h]:
                l = m+1
            else:
                h= m
        return l