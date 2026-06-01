#User function Template for python3

class Solution:
    def sumOfSeries(self,n):
        #code here
        if n==0:
            return
        if n==1:
            return 1
        else:
            return (n**3)+self.sumOfSeries(n-1)