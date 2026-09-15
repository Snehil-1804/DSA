'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
	
class Solution:
    def segregate(self, head):
        #code here
        res=[]
        curr1=head
        while curr1 is not None:
            res.append(curr1.data)
            curr1=curr1.next
        res=sorted(res)

        head_final=Node(res[0])
        curr_final=head_final
        for i in res[1:]:
            curr_final.next=Node(i)
            curr_final=curr_final.next



        return head_final