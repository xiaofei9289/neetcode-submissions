class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        def backtracking(startIndex, path):
            if startIndex >= len(nums):
                return
            for ele in range(startIndex,len(nums)):
                path.append(nums[ele])
                res.append(path.copy())
                backtracking(ele+1,path)
                path.pop()
        backtracking(0,[])
        return res