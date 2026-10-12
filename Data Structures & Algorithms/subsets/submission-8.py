class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        path = []
        self.backtracking(nums,0,path,result)
        return result
    def backtracking(self, nums, startIndex,path, result):
        if startIndex >= len(nums):
            return 
        for i in range(startIndex, len(nums)):
            path.append(nums[i])
            result.append(path.copy())
            self.backtracking(nums, i+1, path, result)
            path.pop()
        