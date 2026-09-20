# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        store = []
        new_node = ListNode(0)
        while head:
            store.append(head)
            head = head.next
        lef = 0 
        rig = len(store)-1
        while lef < rig:
            new_node.next = store[lef]
            new_node = new_node.next
            lef += 1

            new_node.next = store[rig]
            new_node = new_node.next
            rig -= 1
        if lef == rig:
            new_node.next = store[lef]
            new_node = new_node.next
        new_node.next = None