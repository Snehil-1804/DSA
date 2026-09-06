# class Node:
#     def __init__(self, value):
#         self.data = value  # value stored in node
#         self.next = None
#         self.prev = None

class Solution:
    def removeDuplicates(self, headRef):
        curr=headRef 
        while curr:
            if curr.prev and curr.prev.data==curr.data:
                if curr.prev==headRef:
                    curr.prev=None
                    headRef=curr
                else:
                    curr.prev.prev.next=curr
                    curr.prev=curr.prev.prev
            curr=curr.next
        return headRef