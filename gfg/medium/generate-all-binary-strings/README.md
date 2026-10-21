# Generate All Binary

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an integer  **n**. You need to generate all the binary strings of n characters representing bits.

 **Note:**  Return the strings in  ascending order.

 **Examples:** 

```
Input: n = 2
Output: [00, 01, 10, 11]
Explanation: As each position can be either 0 or 1, the total possible combinations are 4.
```

```
Input: n = 3
Output: [000, 001, 010, 011, 100, 101, 110, 111]
Explanation: As each position can be either 0 or 1, the total possible combinations are 8.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-21T12:28:08.553Z  

```py
class Solution:
    
    def solve(self,index,number,result):
        if index>=len(number):
            result.append("".join(number))
            return 
        number[index]="0"
        self.solve(index+1,number,result)
        
        number[index]="1"
        self.solve(index+1,number,result)
    def binstr(self, n):
        # code here
        numbers = ["0"] * n
        result = []
        self.solve(0, numbers, result)
        return result
        
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/generate-all-binary-strings/1)