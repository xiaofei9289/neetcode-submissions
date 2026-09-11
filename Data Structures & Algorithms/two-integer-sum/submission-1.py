class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create a dict which is value:index
        sum_dict={}
        for i in range(len(nums)):
            value = nums[i]
            res=target - value
            
            if res in sum_dict:
                return[sum_dict[res],i]
            sum_dict[value]=i
        