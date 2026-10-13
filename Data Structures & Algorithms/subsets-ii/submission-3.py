class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        sorted_nums = sorted(nums)
        def backtracking(start_index, path):
            if start_index > len(nums):
                return
            res.append(path.copy())
            for i in range(start_index, len(nums)):
                if i > start_index and sorted_nums[i] == sorted_nums[i-1]:
                    continue
                path.append(sorted_nums[i])
                backtracking(i+1,path)
                path.pop()
        backtracking(0,[])
        return res