# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack=[]
        if head is None:
            return None
        cur = head
        while cur:
            stack.append(cur)
            cur=cur.next
        new_head=stack[-1]
        new_cur=stack.pop()
        while stack:
            temp=stack.pop()
            new_cur.next=temp
            new_cur=temp

        new_cur.next=None
        return new_head

