# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.dfs(root)
        return self.res
    

    def dfs(self, root):
        if root is None:
            return 0 
        lef_dep = self.dfs(root.left)
        rig_dep = self.dfs(root.right)
        self.res = max(self.res, lef_dep + rig_dep)
        return 1+ max(lef_dep, rig_dep)