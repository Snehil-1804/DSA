class Solution:
    def leaders(self, arr):
        # code here
        n=len(arr)
        leader=[]
        curr_lead=0
        for i in range(n-1,-1,-1):
            if arr[i]>=curr_lead:
                curr_lead=arr[i]
                leader.append(arr[i])
        leader.reverse() 
        return leader