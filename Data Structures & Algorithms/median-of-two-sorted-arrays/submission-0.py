class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sorted_nums = sorted(nums1 + nums2)

        n = len(sorted_nums)

        if n%2 == 1:
            return float(sorted_nums[n//2])
        else:
            value1 = sorted_nums[n//2]
            value2 = sorted_nums[n//2-1]
            total = value1 + value2

            return float(total/2)