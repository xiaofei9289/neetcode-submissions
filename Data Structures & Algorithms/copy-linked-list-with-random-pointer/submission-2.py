"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node_dict = {None: None}
        cur = head
        while cur:
            node_dict[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        while cur:
            new_node = node_dict[cur]
            new_node.next = node_dict[cur.next]
            new_node.random = node_dict[cur.random]
            cur = cur.next
        return node_dict[head]