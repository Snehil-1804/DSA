''' Structure of linked list Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
class Solution:
    def getCount(self, head):
        # code here
        curr=head
        count=1
        while curr.next is not None:
            count+=1
            curr=curr.next
        return count