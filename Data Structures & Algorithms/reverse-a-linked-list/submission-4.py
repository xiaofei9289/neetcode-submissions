# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre_node=None
        cur_head=head
        while cur_head:
            temp=cur_head.next
            cur_head.next=pre_node
            pre_node=cur_head
            cur_head=temp
        return pre_node