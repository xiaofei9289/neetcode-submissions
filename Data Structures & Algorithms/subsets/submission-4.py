class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        subset = []

        def backtrace(index):
            if index == len(nums):
                result.append(subset.copy())
                return
            subset.append(nums[index])
            backtrace(index+1)
            subset.pop()
            backtrace(index+1)
        backtrace(0)
        return result
        