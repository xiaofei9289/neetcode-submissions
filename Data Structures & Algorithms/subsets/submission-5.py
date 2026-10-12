class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(index, cur):
            if index == len(nums):
                result.append(cur.copy())
                return
            cur.append(nums[index])
            backtrack(index+1, cur)
            cur.pop()
            backtrack(index+1,cur)
        backtrack(0,[])
        return result