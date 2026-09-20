# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return head
        
        
        store = []
        cur =head
        while cur:
            store.append(cur)
            cur = cur.next
        index = len(store) - n
        if index == 0:
            return head.next
        store[index-1].next = store[index].next
        return head

