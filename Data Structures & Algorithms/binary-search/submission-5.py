class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lef = 0
        rig = len(nums)

        while lef < rig:
            mid = (lef + rig) // 2
            if nums[mid] < target:
                lef += 1
            elif nums[mid] >target:
                rig -= 1
            else:
                return mid
        return -1