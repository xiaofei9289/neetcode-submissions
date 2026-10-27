class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i in range(len(nums)):
            for j in map:
                if map[j] == target-nums[i]:
                    return [j,i]
            map[i] = nums[i]

        