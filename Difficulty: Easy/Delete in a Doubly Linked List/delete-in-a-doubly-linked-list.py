""" Structure of a Doubly Linked List Node
class Node:
    def __init__(self, d):
        self.data = d
        self.prev = None
        self.next = None
"""

class Solution:
    def delPos(self, head, x):
        # code here
        if head is None:
            return None
        curr=head
        if x==1:
            head=head.next
            if head is not None:
                head.prev=None
            return head 
        count=1
        while curr is not None and count<x:
            count+=1
            curr=curr.next
        if curr is None:
            return head
        if curr.prev is not None:
            curr.prev.next=curr.next
        if curr.next is not None:
            curr.next.prev=curr.prev
        return head