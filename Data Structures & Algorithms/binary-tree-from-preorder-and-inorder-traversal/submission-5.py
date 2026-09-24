class Solution:

    def buildTree(self, preorder, inorder):

        self.index_map = {}

        for i, val in enumerate(inorder):
            self.index_map[val] = i


        self.pre_idx = 0

        return self.dfs(
            preorder,
            0,
            len(inorder)-1
        )


    def dfs(self, preorder, left, right):

        # 没有节点
        if left > right:
            return None


        # 前序当前位置就是根
        root_val = preorder[self.pre_idx]

        self.pre_idx += 1


        root = TreeNode(root_val)


        # 找根在中序的位置
        mid = self.index_map[root_val]


        # 左子树
        root.left = self.dfs(
            preorder,
            left,
            mid-1
        )


        # 右子树
        root.right = self.dfs(
            preorder,
            mid+1,
            right
        )


        return root