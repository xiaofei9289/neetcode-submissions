class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        def backtracking(start_index, path):
            if start_index >= len(nums):
                return
            for i in range(start_index, len(nums)):
                path.append(nums[i])
                res.append(path.copy())
                backtracking(i+1, path)
                path.pop()
        backtracking(0,[])
        return res