# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        self.nodes = []
        cur = head

        while cur:
            self.nodes.append(cur)
            cur = cur.next

        self.rec(0, len(self.nodes) - 1)


    def rec(self,left, right):
        if left > right:
            return None
        if left == right:
            self.nodes[left].next = None
            return self.nodes[left]
        
        middle = self.rec(left + 1, right - 1)

      
        self.nodes[left].next = self.nodes[right]
        self.nodes[right].next = middle

        return self.nodes[left]

  