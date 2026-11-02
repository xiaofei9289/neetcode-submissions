class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        store = set(nums)
        if len(store) == len(nums):
            return False
        else:
            return True