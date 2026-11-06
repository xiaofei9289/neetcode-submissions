from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []

        for rig in range(len(nums)):
            lef = rig - k + 1

            # 1. 删除窗口左边已经过期的索引
            while q and q[0] < lef:
                q.popleft()

            # 2. 保证队列对应的数字单调递减
            while q and nums[q[-1]] <= nums[rig]:
                q.pop()

            # 3. 添加当前数字的索引
            q.append(rig)

            # 4. 窗口形成后记录最大值
            if lef >= 0:
                res.append(nums[q[0]])

        return res