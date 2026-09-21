''' structure of linked list Node
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''
class Solution:
    def addOne(self,head):
        head = self.reverseAll(head)
        carry = 1
        temp = head
        while temp is not None:
            temp.data = temp.data + carry
            if temp.data < 10:
                carry = 0
                break
            else:
                temp.data = 0
                carry = 1
            temp = temp.next
        if carry == 1:
            newNode = Node(1)
            temp = self.reverseAll(head)
            newNode.next = temp
            return newNode
        temp = self.reverseAll(head)
        return temp
    def reverseAll(self,head):
        temp = head
        prev = None
        while temp is not None:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
        return prev