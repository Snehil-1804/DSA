class Solution:
    def findMean(self, arr):
        n=len(arr)
        add=sum(arr)
        avg=add//n
        return avg