''' Structure of Doubly Linked List Node
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None

'''

class Solution:
    def insertAtPos(self, head, p, x):
        # Create the new node to insert
        new_node = Node(x)

        # Traverse to the p-th node
        curr = head
        for _ in range(p):
            if curr:
                curr = curr.next

        # If position is invalid/out of bounds, return head
        if not curr:
            return head

        # Adjust pointers to insert new_node after curr
        new_node.next = curr.next
        new_node.prev = curr

        # If curr is not the last node, update the next node's prev pointer
        if curr.next:
            curr.next.prev = new_node

        # Point curr's next to the new node
        curr.next = new_node

        return head