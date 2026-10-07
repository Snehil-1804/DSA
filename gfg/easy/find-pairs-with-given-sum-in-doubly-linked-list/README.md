# Pair Sum in Sorted Doubly Linked List

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a sorted doubly linked list containing distinct positive integers and an integer target, find all pairs of nodes whose values add up to target.

 **Examples :** 

```
Input:

target = 7
Output: [[1, 6], [2, 5]]
Explanation: There are two pairs (1, 6) and (2,5) with sum 7.
```

```
Input: 

target = 6
Output: [[1, 5]]
Explanation: There is one pairs  (1, 5) with sum 6.

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-07T12:12:37.662Z  

```py
# Structure of Doubly Linked List Node
'''
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
'''

class Solution:
    def givenSumPairs(self, head, target):
        result=[]
        left=head
        right=head
        while right.next is not None:
            right=right.next
            
        
        while left is not None and right is not None and left.data<right.data:
            total=left.data+right.data
            
            if total==target:
                result.append([left.data,right.data])
                left=left.next
                right=right.prev
                
            elif total>target:
                right=right.prev
            
            else:
                left=left.next
            
        return result
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/find-pairs-with-given-sum-in-doubly-linked-list/1)