class Solution:
    def maxArea(self, heights: List[int]) -> int:
        p1 = 0
        p2 = len(heights)-1
        max_area = 0
        while p1 < p2:
            h = min(heights[p1],heights[p2])
            l = p2 - p1 
            area = h * l
            max_area = max(max_area, area)
            if heights[p1]< heights[p2]:
                p1 += 1
            else:
                p2 -= 1
        return max_area