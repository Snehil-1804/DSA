#User function Template for python3
class Solution:
	def reverseSubArray(self,arr,l,r):
		result=[]
        s=r
        # r=3
        for i in range(len(arr)):
            if i>=l-1 and i<s: 
                result.append(arr[r-1])
                r-=1
            else:
                result.append(arr[i])
        return result