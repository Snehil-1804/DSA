# Generate Parentheses

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given `n` pairs of parentheses, write a function to  *generate all combinations of well-formed parentheses*.

 

Original
Python3
 **Example 1:** 

```
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

```

 **Example 2:** 

```
Input: n = 1
Output: ["()"]

```

 

 **Constraints:** 

- 1 <= n <= 8

## Solution

**Language:** Python  
**Runtime:** 0 ms  
**Memory:** 19.2 MB  
**Submitted:** 2026-11-18T08:00:16.163Z  

```py
class Solution:
    def solve(self,index,total,bracket,result):
        if index>=len(bracket):
            if total==0:
                result.append(".".join(bracket))
            return
        if total>len(bracket)//2:
            return
        elif total<0:
            return
        bracket[index]="("
        sum=total+1
        self.solve(index+1,sum,bracket,result)
        bracket[index]=")"
        sum=total-1
        self.solve(index+1,total,bracket,result)
        return result

    def generateParenthesis(self, n: int) -> list[str]:
        bracket=[""]*(n*2)
        result=[]
        self.solve(0,0,bracket,result)

        
```

---

[View on LeetCode](https://leetcode.com/problems/generate-parentheses/)