# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.depth(root)
        return self.res
    
    def depth(self, node):
        if node is None:
            return 0
        
        left = self.depth(node.left)
        right = self.depth(node.right)

        self.res = max(self.res, left + right)
        return max(left,right)+1