class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for ele in nums:
            res += [subset + [ele] for subset in res]
        return res