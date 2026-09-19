class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()
        for ele in nums:
            if ele not in seen:
                seen.add(ele)
            else:
                return ele
        