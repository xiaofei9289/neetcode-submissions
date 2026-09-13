class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = list()
        for i in range(len(nums)):
            ele = nums[i]
            needed = target - ele

            if needed in seen:
                return[seen.index(needed),i]
            seen.append(ele)