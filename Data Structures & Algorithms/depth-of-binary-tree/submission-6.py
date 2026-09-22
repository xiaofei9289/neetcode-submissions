# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        lef_len = self.maxDepth(root.left)
        rig_len = self.maxDepth(root.right)
        dep = max(lef_len,rig_len)+1
        return dep