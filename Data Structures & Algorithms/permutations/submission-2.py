class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        final_res = []
        def backtracking(path):
            if len(path) == len(nums):
                final_res.append(path.copy())
                return
            for i in range(len(nums)):
                if nums[i] in path:
                    continue
                path.append(nums[i])
                backtracking(path)
                path.pop()
        backtracking([])
        return final_res