class Solution:

    def levelOrder(self, root):

        res = []

        self.dfs(root,0,res)

        return res


    def dfs(self,node,level,res):

        if not node:
            return

        if level == len(res):
            res.append([])

        res[level].append(node.val)

        self.dfs(node.left, level+1,res)
        self.dfs(node.right, level+1,res)