class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        def backtracking(start_index, path, total):
            if total == target:
                result.append(path.copy())
            if start_index>len(nums) or total > target:
                return
            for i in range(start_index, len(nums)):
                path.append(nums[i])
                backtracking(i, path, total+nums[i])
                path.pop()
        backtracking(0,[],0)
        return result