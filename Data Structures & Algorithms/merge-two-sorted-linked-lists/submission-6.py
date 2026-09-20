# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        store = []
        while list1:
            store.append(list1)
            list1=list1.next
        while list2:
            store.append(list2)
            list2=list2.next
        store.sort(key=lambda node:node.val)
        head = ListNode(0)
        cur = head
        for ele in store:
            cur.next = ele
            cur = ele
        cur.next = None
        return head.next