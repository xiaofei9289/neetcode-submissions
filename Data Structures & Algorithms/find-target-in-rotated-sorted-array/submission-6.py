import bisect
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        while left < right:
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        sec_point=left

        if target<=nums[-1]:
            low,high=sec_point,len(nums)
        else:
            low,high=0,sec_point
        index=bisect.bisect_left(nums,target,low,high)

        if index < high and nums[index]==target:
            return index
        return -1


        