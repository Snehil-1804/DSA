# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def findmid(self,head):
        slow=head
        fast=head.next
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
        return slow

    def mergeTwoList(self,l1,l2):
        new_node=ListNode(None)
        temp=new_node
        while l1 is not None and l2 is not None:
            if l1.val<l2.val:
                temp.next=l1
                temp=l1
                l1=l1.next
            else:
                temp.next=l2
                temp=l2
                l2=l2.next
        if l1 is not None:
            temp.next=l1
        else:
            temp.next=l2
        return new_node.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        middle = self.findmid(head)
        right = middle.next
        middle.next = None  
        left=head
        left_side=self.sortList(left)
        right_side=self.sortList(right)

        return self.mergeTwoList(left_side,right_side)

        