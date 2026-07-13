class Solution:
    def maxLength(self, arr):
        # code here
        n=len(arr)
        d=dict()
        maxlen=0
        curr_len=0
        
        for x in range(n):
            curr_len+=arr[x]
            if arr[x]==0 and maxlen==0:
                maxlen=1
            elif curr_len==0:
                maxlen=x+1
            elif curr_len in d:
                maxlen=max(maxlen,x-d[curr_len])
            else:
                d[curr_len]=x
        return maxlen