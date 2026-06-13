#User function Template for python3

class Solution:
    def rotate(self, arr):
        n=len(arr)
        last=arr[n-1]
        for i in range(n-2,-1,-1):
            arr[i+1]=arr[i]
        arr[0]=last