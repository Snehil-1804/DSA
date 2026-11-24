# Combination Sum II

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a collection of candidate numbers (`candidates`) and a target number (`target`), find all unique combinations in `candidates` where the candidate numbers sum to `target`.

Each number in `candidates` may only be used  **once**  in the combination.

 **Note:**  The solution set must not contain duplicate combinations.

 

Original
Python3
 **Example 1:** 

```
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

```

 **Example 2:** 

```
Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]

```

 

 **Constraints:** 

- 1 <= candidates.length <= 100
- 1 <= candidates[i] <= 50
- 1 <= target <= 30

## Solution

**Language:** Python  
**Runtime:** 1 ms (beats 95.02%)  
**Memory:** 19.4 MB (beats 77.79%)  
**Submitted:** 2026-11-24T10:29:28.874Z  

```py

class Solution:
    def backtrack(self, index, total, result, subset, nums, target):
        if total == 0:
            result.append(subset.copy())
            return

        if total < 0:
            return

        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i-1]:
                continue

            if nums[i] > total:
                break

            subset.append(nums[i])
            self.backtrack(i+1, total-nums[i], result, subset, nums, target)
            subset.pop()

    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        subset = []
        result = []

        self.backtrack(0, target, result, subset, candidates, target)

        return result

```

---

[View on LeetCode](https://leetcode.com/problems/combination-sum-ii/)