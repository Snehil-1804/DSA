class Solution:
    def sumOfAP(self, n, a, d):
        # code here
        ans = n*(2*a+(n-1)*d)//2
        return ans