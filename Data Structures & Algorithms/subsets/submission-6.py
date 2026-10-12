class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrace(i, cur):
            if i == len(nums):
                res.append(cur.copy())
                return
            cur.append(nums[i])
            backtrace(i+1,cur)
            cur.pop()
            backtrace(i+1,cur)
        backtrace(0,[])
        return res