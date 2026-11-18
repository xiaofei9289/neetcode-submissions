class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1,nums2 = nums2,nums1
        
        n1 = len(nums1)
        n2 = len(nums2)

        l = 0 
        r = n1

        while l <= r:
            mid1 = (l + r)//2
            mid2 = (n1 + n2)//2 - mid1
            lef1_value = nums1[mid1-1] if mid1 > 0 else float("-inf")
            rig1_value = nums1[mid1] if mid1 < n1 else float("inf")
            lef2_value = nums2[mid2-1] if mid2 > 0 else float("-inf")
            rig2_value = nums2[mid2] if mid2 < n2 else float("inf")

            if lef1_value > rig2_value:
                r = mid1 - 1
            elif lef2_value > rig1_value:
                l = mid1 + 1
            else:
                if(n1+n2)%2==1:
                    return float(min(rig1_value,rig2_value))
                else:
                    return (max(lef1_value, lef2_value) + min(rig1_value, rig2_value)) / 2


        