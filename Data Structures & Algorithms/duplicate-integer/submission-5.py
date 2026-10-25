class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        store = set()
        for ele in nums:
            if ele in store:
                return True
            store.add(ele)
        return False