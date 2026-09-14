class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        for i in range(len(nums)-2):
            seen = set()
            for j in range(i+1, len(nums)):
                target = -(nums[i]+nums[j])
                if target in seen:
                    res.add(tuple(sorted([nums[i],nums[j],target])))
                seen.add(nums[j])
        return [list(ele) for ele in res]
                