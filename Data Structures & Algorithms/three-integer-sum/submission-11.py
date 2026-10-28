class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        res = []
        n = len(nums)
        for i in range(len(nums)-2):
            p1 = i+1
            p2 = len(nums)-1
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue

            p1 = i + 1
            p2 = n - 1

            while p1 < p2:
                sum = sorted_nums[p1] + sorted_nums[p2] + sorted_nums[i]
                if sum > 0:
                    p2 -= 1
                elif sum < 0:
                    p1 += 1
                else:
                    res.append([sorted_nums[i], sorted_nums[p1], sorted_nums[p2]])
                    p1 += 1
                    p2 -= 1
                    while p1 < p2 and sorted_nums[p1] == sorted_nums[p1 - 1]:
                        p1 += 1
                    while p1 < p2 and sorted_nums[p2] == sorted_nums[p2 + 1]:
                        p2 -= 1
        return res