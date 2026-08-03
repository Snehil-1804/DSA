class Solution:
       
    def lcm(self, a, b):
        x=a
        y=b
        
        while b!=0:
            a,b=b,a%b
        gcd=a
        
        lcm=(x*y)//gcd
        return lcm