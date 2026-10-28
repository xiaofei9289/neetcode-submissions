class Solution:
    def maxArea(self, heights: List[int]) -> int:
        lef = 0
        rig = len(heights) - 1
        res = 0

        while lef < rig:
            h = min(heights[lef],heights[rig])
            l = rig - lef

            area = h * l
            res = max(res, area)

            if heights[lef] < heights[rig]:
                lef += 1
            else:
                rig -= 1
        return res