class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lef = 0
        rig = len(nums) - 1
        while lef <= rig:
            mid = (lef + rig) // 2

            if nums[mid] == target:
                return mid
            
            if nums[lef] <= nums[mid]:
                if nums[lef] <= target < nums[mid]:
                    rig = mid - 1
                else:
                    lef = mid + 1
            
            else:
                if nums[mid] < target <= nums[rig]:
                    lef = mid + 1
                else:
                    rig = mid - 1

        return -1