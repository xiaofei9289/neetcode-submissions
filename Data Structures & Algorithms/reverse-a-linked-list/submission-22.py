# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre_node = None
        cur_node = head

        while cur_node:
            temp = cur_node.next
            cur_node.next = pre_node
            pre_node = cur_node
            cur_node = temp
        return pre_node
