class Solution:
    def maxArea(self, heights: List[int]) -> int:
        p1 = 0
        p2 = len(heights) - 1
        res = 0

        while p1<p2:
            h = min(heights[p1],heights[p2])
            l = p2 - p1

            area = h * l
            res = max(res, area)
            if heights[p1] < heights[p2]:
                p1 += 1
            else:
                p2 -= 1
        return res