# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        stack = [(root,float("-inf"))]
        count = 0

        while stack:
            node, max_value = stack.pop()

            if node.val>=max_value:
                count += 1
            new_max = max(node.val, max_value)
            if node.left:
                stack.append((node.left,new_max))
            if node.right:
                stack.append((node.right,new_max))
        return count


        