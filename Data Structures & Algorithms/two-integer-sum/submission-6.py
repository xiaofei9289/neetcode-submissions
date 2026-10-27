class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            cur = nums[i]
            res = target - cur

            if res in map:
                return [map[res],i]
            map[cur] = i