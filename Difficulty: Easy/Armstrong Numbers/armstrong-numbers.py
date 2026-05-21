#User function Template for python3

class Solution:
    def armstrongNumber (self, n):
        # code here 
        num=n
        total=0
        nod=len(str(n))
        while num!=0:
            ld=num%10
            total=total+(ld**nod)
            num=num//10
        
        if total==n:
            return True
        else:
            return False