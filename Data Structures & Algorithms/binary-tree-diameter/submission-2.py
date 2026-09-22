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
        res = 0 
        stack = [root]
        while stack:
            node = stack.pop()
            lef_dep = self.get_depth(node.left)
            rig_dep = self.get_depth(node.right)
            res = max(res, lef_dep + rig_dep)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return res
        
        
    def get_depth(self, root)-> int:
        if root is None:
            return 0
            
        left = self.get_depth(root.left)
        right = self.get_depth(root.right)

        return max(left,right)+1