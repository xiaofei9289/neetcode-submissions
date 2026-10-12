class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def backtracking(start_index, path):
            res.append(path.copy())
            for i in range(start_index,len(nums)):
                if i > start_index and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                backtracking(i+1,path)
                path.pop()
        backtracking(0,[])
        return res