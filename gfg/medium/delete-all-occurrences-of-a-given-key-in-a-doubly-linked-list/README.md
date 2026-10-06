# Delete All Occurrences in DLL

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given the head of a doubly Linked List and a key  **x** . Delete all occurrences of the given key x if it is present and return the new DLL.

 **Examples:** 

```
Input: 2<->2<->10<->8<->4<->2<->5<->2, x = 2

Output:  10<->8<->4<->5

Explanation: 
All Occurrences of 2 have been deleted.

```

```
Input: head = 9<->1<->3<->4<->5<->1<->8<->4, x = 9

Output: 1<->3<->4<->5<->1<->8<->4

Explanation: 
All Occurrences of 9 have been deleted.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-06T14:56:23.509Z  

```py
# Structure of the doubly linked list Node 
# class Node:
#     def __init__(self, x):
#         self.data = x
#         self.next = None
#         self.prev = None

class Solution:
    def deleteAllOccurOfX(self, head, x):
        # code here
        if head.next is None and head.data==x:
            return None
        temp=head
        prev=None
        new_head=head
        
        while temp is not None:
            if temp.data==x:
                if prev is not None:
                    prev.next=temp.next
                if temp.next is not None:
                    temp.next.prev=prev
                if temp==new_head:
                    new_head = new_head.next
                temp=temp.next
            else:
                prev=temp
                temp=temp.next
            
        return new_head
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/delete-all-occurrences-of-a-given-key-in-a-doubly-linked-list/1)