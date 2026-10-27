class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        de_dupe = set(nums)
        if len(de_dupe) != len(nums):
            return True
        else:
            return False