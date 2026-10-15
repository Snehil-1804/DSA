# Subsets

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an integer array `nums` of  **unique**  elements, return  *all possible*   *subsets*   *(the power set)*.

The solution set  **must not**  contain duplicate subsets. Return the solution in  **any order**.

 

 **Example 1:** 

```
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

```

 **Example 2:** 

```
Input: nums = [0]
Output: [[],[0]]

```

 

 **Constraints:** 

- 1 <= nums.length <= 10
- -10 <= nums[i] <= 10
- All the numbers of nums are unique.

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 19.3 MB (beats 92.61%)  
**Submitted:** 2026-10-15T14:59:51.071Z  

```py
class Solution:
    def solve(self,i,nums,subset,res):
        if i>=len(nums):
            res.append(subset.copy())
            return res
        subset.append(nums[i])
        self.solve(i+1,nums,subset,res)
        subset.pop()
        self.solve(i+1,nums,subset,res)

    def subsets(self, nums: list[int]) -> list[list[int]]:
        res=[]
        subset=[]
        self.solve(0,nums,subset,res)
        return res

```

---

[View on LeetCode](https://leetcode.com/problems/subsets/)