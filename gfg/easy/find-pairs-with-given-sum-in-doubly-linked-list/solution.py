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