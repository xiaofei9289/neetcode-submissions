class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtracking(path):
            if len(path) == len(nums):
                res.append(path.copy())
                return
            for ele in nums:
                if ele in path:
                    continue
                path.append(ele)
                backtracking(path)
                path.pop()
        backtracking([])
        return res