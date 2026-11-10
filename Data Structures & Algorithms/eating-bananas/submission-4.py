class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1 
        r = max(piles)

        while l < r:
            mid = (l+r)//2
            time = 0

            for ele in piles:
                time = (ele + mid - 1)//mid + time
            if time <= h:
                r = mid
            else:
                l = mid + 1
        return l