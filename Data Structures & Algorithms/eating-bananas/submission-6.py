class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lef = 1
        rig = max(piles)

        while lef < rig:
            mid = (lef + rig) // 2
            time = 0

            for ele in piles:
                time = math.ceil(ele / mid) + time
            if time <= h:
                rig = mid
            else:
                lef = mid + 1
        return lef