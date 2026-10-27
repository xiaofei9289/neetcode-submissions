class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        store = set()
        for ele in nums:
            store.add(ele)
        if len(nums) == len(store):
            return False
        else:
            return True