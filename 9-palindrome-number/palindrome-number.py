class Solution:
    def isPalindrome(self, x: int) -> bool:
        num=x
        result=0
        if num<0:
            return False
        while num>0:
            id = num%10
            result=(result*10)+id
            num=num//10
        if(result==x):
            return True
        else:
            return False