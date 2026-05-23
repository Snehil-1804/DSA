class Solution:
    def countFactors (self, n):
        # code here
        result=[]
        for i in range(1,n//2+1):
            if n%i==0:
                result.append(i)
        result.append(n)
        return len(result)