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
        while cur is not None:
            stack.append(cur)
            cur=cur.next
        new_head=stack.pop()
        new_cur=new_head
        while stack:
            next_node=stack.pop()
            new_cur.next=next_node
            new_cur=next_node
        new_cur.next = None
        return new_head
        