# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.arr = []
        self.inorder(root)
        return self.arr[k-1]

    def inorder(self, node):
        if not node:
            return
        self.inorder(node.left)
        self.arr.append(node.val)
        self.inorder(node.right)