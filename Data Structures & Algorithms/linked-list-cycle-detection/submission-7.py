# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow_one = head
        fast_one = head

        while fast_one and fast_one.next:
            slow_one = slow_one.next
            fast_one = fast_one.next.next
            if slow_one == fast_one:
                return True
        return False