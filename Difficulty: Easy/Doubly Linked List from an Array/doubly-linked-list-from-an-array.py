''' class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
'''

class Solution:
    def createDLL(self, arr):
       # code here
        head = Node(arr[0])
        temp = head
        for i in range(1, len(arr)):
            newNode = Node(arr[i])
            newNode.prev = temp
            temp.next = newNode
            temp = temp.next
            
        return head