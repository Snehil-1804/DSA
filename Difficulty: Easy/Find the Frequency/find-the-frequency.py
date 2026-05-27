"""
You're given an array (arr)
Return the frequency of element x in the given array
"""
class Solution:
    def findFrequency(self, arr, x):
        
        # code here
        frequency={}
        
        for i in arr:
            if x not in arr:
                return 0
            frequency[i]=frequency.get(i,0)+1
        return frequency.get(x)