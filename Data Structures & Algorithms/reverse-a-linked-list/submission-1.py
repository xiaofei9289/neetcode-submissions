# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        stack=[]
        cur=head
        while cur:
            stack.append(cur)
            cur=cur.next
        new_head=stack.pop()
        cur=new_head
        while stack:
            node= stack.pop()
            cur.next=node
            cur=node
        cur.next=None   
        return new_head


        