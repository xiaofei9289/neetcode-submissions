class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        for i in range(len(nums)-2):
            seen = set()
            for j in range(i+1,len(nums)):
                need = -nums[i]-nums[j]

                if need in seen:
                    target=tuple(sorted([nums[i],nums[j],need]))
                    res.add(target)
                seen.add(nums[j])
        return [list(ele) for ele in res]