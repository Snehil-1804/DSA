# Check K-th Bit

![Difficulty](https://img.shields.io/badge/Difficulty-Basic-red)

## Problem

Given two positive integer  **n** and   **k**, check if the  **kth**  index bit of  **n** is set or not. A bit is called set if it is 1. 

 **Examples :** 

```
Input: n = 4, k = 0
Output: false
Explanation: Binary representation of 4 is 100, in which 0th index bit from LSB is not set. So, return false.
```

```
Input: n = 4, k = 2
Output: true
Explanation: Binary representation of 4 is 100, in which 2nd index bit from LSB is set. So, return true.
```

```
Input: n = 500, k = 3
Output: false
Explanation: Binary representation of 500 is 111110100, in which 3rd index bit from LSB is not set. So, return false.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-08T16:27:06.513Z  

```py
class Solution:
    def checkKthBit(self, n, k):
        # code here
        if (n&(1<<k))!=0:
            return True
        else:
            return False
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/check-whether-k-th-bit-is-set-or-not-1587115620/1)