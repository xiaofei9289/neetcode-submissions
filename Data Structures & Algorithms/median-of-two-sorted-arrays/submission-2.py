class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)>len(nums2):
            nums1,nums2 = nums2,nums1
        
        n1 = len(nums1)
        n2 = len(nums2)

        low = 0
        high = n1

        while low<=high:
            i = (low+high)//2
            j = (n1+n2+1)//2 - i

            lef1 = nums1[i-1] if i>0 else float("-inf")
            rig1 = nums1[i] if i<n1 else float("inf")
            lef2 = nums2[j-1] if j>0 else float("-inf")
            rig2 = nums2[j] if j<n2 else float("inf")

            if lef1 <= rig2 and lef2 <= rig1:
                if(n1+n2)%2==1:
                    return max(lef1,lef2)
                return (max(lef1,lef2) + min(rig1,rig2))/2
            elif lef1 > rig2:
                high = i-1
            else:
                low = i+1