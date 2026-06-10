class Solution:
    def largest(self, arr):
        # code here
        largest=float('-inf')
        for i in range(len(arr)):
            largest=max(largest,arr[i])
        return largest 