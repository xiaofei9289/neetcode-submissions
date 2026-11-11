class Solution:
    def findMin(self, nums: List[int]) -> int:
        lef = 0
        rig = len(nums) - 1

        val_lef = nums[lef]
        val_rig = nums[rig]

        if val_lef < val_rig:
            return val_lef
        
        else:
            while lef < rig:
                mid = (lef + rig) // 2
                if nums[mid] >= val_lef:
                    lef = mid + 1
                else:
                    rig =mid

            return nums[lef]