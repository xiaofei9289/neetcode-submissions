class Solution:
    def findMin(self, nums: List[int]) -> int:
        lef = 0
        rig = len(nums) - 1

        while lef < rig:
            mid = (lef + rig) // 2
            if nums[mid] > nums[rig]:
                lef = mid + 1
            else:
                rig = mid
        return nums[lef]