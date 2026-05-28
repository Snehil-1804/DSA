class Solution:
    def frequencyCount(self, arr):
        #  code here
        noe=len(arr)
        hash_list=[0]*noe
        for index in arr:
            hash_list[index-1]+=1
        return hash_list
