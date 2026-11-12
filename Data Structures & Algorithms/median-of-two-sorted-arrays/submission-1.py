class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)

        mid1 = mid2 = 0
        merged = []
        while mid1 < n1 and mid2 < n2:
            if nums1[mid1] <= nums2[mid2]:
                merged.append(nums1[mid1])
                mid1 += 1

            else:
                merged.append(nums2[mid2])
                mid2 += 1
        merged.extend(nums1[mid1:])
        merged.extend(nums2[mid2:])

        total = n1 + n2
        if total % 2 == 1:
            return float(merged[total//2])
        else:
            return (merged[total//2-1]+merged[total//2])/2

