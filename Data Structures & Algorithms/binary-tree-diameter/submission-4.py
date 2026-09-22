# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left = self.maxHeight(root.left)
        right = self.maxHeight(root.right)
        res = left + right

        sub = max(self.diameterOfBinaryTree(root.left),self.diameterOfBinaryTree(root.right))

        return max(res, sub)

    def maxHeight(self, root):
        if root is None:
            return 0
        left_length = self.maxHeight(root.left)
        right_length = self.maxHeight(root.right)

        return 1 + max(left_length, right_length)
        