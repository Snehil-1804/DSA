""" Structure of Doubly Linked List Node
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
"""

class Solution:
    def reverse(self, head):
        # code here
        
        if head.next is None:
            return head
        curr=head
        prev=None
        
        while curr is not None:
            front=curr.next
            curr.next=prev
            curr.prev=front
            prev=curr
            curr=front
        return prev