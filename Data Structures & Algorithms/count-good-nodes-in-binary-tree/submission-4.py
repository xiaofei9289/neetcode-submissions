# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root,float("-inf"))

    def dfs(self, root, max_val):
        if not root:
            return 0 
        count = 0 
        if root.val>=max_val:
            count = 1
        max_val =max(max_val,root.val)
        left_count = self.dfs(root.left,max_val)
        right_count = self.dfs(root.right,max_val)

        return count+left_count+right_count