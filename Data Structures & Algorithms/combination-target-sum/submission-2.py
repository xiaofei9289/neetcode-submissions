class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtracking(start_index, path, sum):
            if sum == target:
                res.append(path.copy())
                return
            if sum > target:
                return 
            for i in range(start_index, len(nums)):
                path.append(nums[i])
                backtracking(i,path, sum+nums[i])
                path.pop()
        backtracking(0,[],0)
        return res