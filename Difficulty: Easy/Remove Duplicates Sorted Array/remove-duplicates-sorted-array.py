class Solution:
    def removeDuplicates(self, arr):
        # code here 
        return list(dict.fromkeys(arr))
