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
**Memory:** 18.8 MB  
**Submitted:** 2026-11-18T08:01:18.613Z  

```py

class Solution:
    def solve(self, index, total, bracket, result, n):
        if index == len(bracket):
            if total == 0:
                result.append("".join(bracket))
            return

        if total < 0 or total > n:
            return

        bracket[index] = "("
        self.solve(index + 1, total + 1, bracket, result, n)

        bracket[index] = ")"
        self.solve(index + 1, total - 1, bracket, result, n)

    def generateParenthesis(self, n: int) -> list[str]:
        bracket = [""] * (2 * n)
        result = []
        self.solve(0, 0, bracket, result, n)
        return result

```

---

[View on LeetCode](https://leetcode.com/problems/generate-parentheses/)