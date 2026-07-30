class Solution:
    def firstNonRepeating(self, arr): 
        n=len(arr)
        mydict={}
        for i in arr:
            mydict[i]=mydict.get(i,0)+1
        
        for i in arr:
            if mydict[i]==1:
                return i
        return 0