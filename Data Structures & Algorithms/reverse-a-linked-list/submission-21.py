# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        pre = None
        cur = head

        while cur.next:
            tem = cur.next
            cur.next = pre
            pre = cur
            cur = tem
        cur.next = pre
        return cur
        