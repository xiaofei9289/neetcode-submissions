class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_dict = {}
        for i in range(len(nums)):
            cur_value = nums[i]
            res = target - cur_value

            if res in sum_dict:
                return [sum_dict[res], i]
            sum_dict[cur_value] = i
        