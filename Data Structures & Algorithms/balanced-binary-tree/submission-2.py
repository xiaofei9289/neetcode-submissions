# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        lef_height = self.nodeHeight(root.left)
        rig_height = self.nodeHeight(root.right)
        if abs(lef_height - rig_height)>1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
    
    def nodeHeight(self, node):
        if node is None:
            return 0
        l_height = self.nodeHeight(node.left)
        r_height = self.nodeHeight(node.right)

        return 1 + max(l_height, r_height)
        