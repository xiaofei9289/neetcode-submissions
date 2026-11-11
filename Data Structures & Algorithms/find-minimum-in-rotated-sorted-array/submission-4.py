class Solution:
    def findMin(self, nums: List[int]) -> int:
        lef = 0 
        rig = len(nums) - 1
        while lef <= rig:
            if nums[lef] <= nums[rig]:
                return nums[lef]
            mid = (lef + rig) // 2
            if nums[lef] <= nums[mid]:
                lef = mid + 1
            else:
                rig = mid
        return nums[lef]