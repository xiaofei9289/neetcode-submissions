# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        dummy_head = head
        cur = head.next
        dummy_head.next = None
        while cur:
            temp = cur.next
            cur.next = dummy_head
            dummy_head = cur
            cur = temp
        return dummy_head



