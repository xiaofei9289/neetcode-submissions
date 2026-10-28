class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        res = []
        n = len(nums)
        for i in range(len(nums)-2):
            
            if i > 0 and sorted_nums[i] == sorted_nums[i-1]:
                continue 
            
            lef = i + 1
            rig = n - 1

            while lef < rig:
                total = sorted_nums[i] + sorted_nums[lef] + sorted_nums[rig]

                if total > 0 :
                    rig -= 1
                elif total < 0 :
                    lef += 1
                else:
                    res.append([sorted_nums[i], sorted_nums[lef], sorted_nums[rig]])
                    lef += 1
                    rig -= 1
                    while lef < rig and sorted_nums[lef] == sorted_nums[lef-1]:
                        lef += 1

                    while lef < rig and sorted_nums[rig] == sorted_nums[rig+1]:
                        rig -= 1

        return res