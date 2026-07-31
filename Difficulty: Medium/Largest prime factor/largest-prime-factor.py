class Solution:
    def largestPrimeFactor(self, n):
        ans = 1

        while n % 2 == 0:
            ans = 2
            n //= 2

        i = 3
        while i * i <= n:
            while n % i == 0:
                ans = i
                n //= i
            i += 2

        if n > 2:
            ans = n

        return ans