class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store_set = {}
        for i in range(len(nums)):
            goal = target - nums[i]
            if goal in store_set:
                return [store_set.get(goal),i]
            store_set[nums[i]] = i