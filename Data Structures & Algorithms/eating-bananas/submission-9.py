class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = []

        while l <= r:
            mid = (l + r) // 2
            time = 0
            for ele in piles:
                time = time + math.ceil(ele/mid)
            
            if time <= h:
                res.append(mid)
                r = mid - 1
            else:
                l = mid + 1
        return min(res)