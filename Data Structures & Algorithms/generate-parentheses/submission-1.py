class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtracking(path, left, right):
            if left == n and right == n:
                res.append(path)
                return
            if left<n:
                backtracking(path+"(",left+1,right)
            if right<left:
                backtracking(path+")",left,right+1)
        backtracking("",0,0)
        return res