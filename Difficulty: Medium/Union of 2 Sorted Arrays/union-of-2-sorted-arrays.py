class Solution:
    def findUnion(self, a, b):
        # code here 
        n=len(a)
        m=len(b)
        i=0
        j=0
        result=[]
        while i<n and j<m:
            if n==0:
                return b
            elif m==0:
                return a
            if a[i]<=b[j]:
                if len(result)==0 or result[-1]!=a[i]:
                    result.append(a[i])
                i+=1
            else:
                if len(result)==0 or result[-1]!=b[j]:
                    result.append(b[j])
                j+=1
        while i<n:
            if len(result)==0 or result[-1]!=a[i]:
                result.append(a[i])
            i+=1
        while j<m:
            if len(result)==0 or result[-1]!=b[j]:
                result.append(b[j])
            j+=1
        return result