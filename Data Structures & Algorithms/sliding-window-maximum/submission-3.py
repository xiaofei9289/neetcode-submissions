class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        lef = [0] * n
        rig = [0] * n

        for i in range(n):
            if i%k == 0:
                lef[i] = nums[i]
            else:
                lef[i] = max(lef[i-1], nums[i])

        for i in range(n-1,-1,-1):
            if i == n-1 or (i+1)% k ==0:
                rig[i] = nums[i]
            else:
                rig[i] = max(rig[i+1],nums[i])

        res = []
        for i in range(n-k+1):
            res.append(max(rig[i], lef[i+k-1]))

        return res