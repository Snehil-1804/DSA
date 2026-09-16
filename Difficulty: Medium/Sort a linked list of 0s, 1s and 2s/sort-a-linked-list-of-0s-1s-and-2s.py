'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
	
class Solution:
    def segregate(self, head):
        if head is None or head.next is None:
            return head
        zero_head=Node(None)
        one_head=Node(None)
        two_head=Node(None)
        zero=zero_head
        one=one_head
        two=two_head
        
        temp=head 
        while temp is not None:
            next_node = temp.next
            temp.next = None
            if temp.data==0:
                zero.next=temp
                zero=temp
            elif temp.data==1:
                one.next=temp
                one=temp
            else:
                two.next=temp
                two=temp
            temp=next_node
        if one_head.next is not None:
            zero.next=one_head.next
            one.next=two_head.next
        else:
            zero.next=two_head.next
        # one.next=two_head.next
        # two_head=None
        
        return zero_head.next