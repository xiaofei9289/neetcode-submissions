# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        cur1=list1
        cur2=list2
        res=ListNode()
        prev=res
        while cur1 and cur2:
            if cur1.val<=cur2.val:
                prev.next=cur1
                cur1=cur1.next
            else:
                prev.next=cur2
                cur2=cur2.next
            prev=prev.next
        if cur1:
            prev.next=cur1
        else:
            prev.next=cur2
        return res.next

        