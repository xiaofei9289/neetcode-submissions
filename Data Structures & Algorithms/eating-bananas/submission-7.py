class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l = 1
        r = max(piles)

        while l < r:
            consume_time = 0
            mid = (l + r) // 2
            for ele in piles:
                consume_time = math.ceil(ele/mid) + consume_time

            if consume_time <= h:
                r = mid
            else:
                l = mid + 1
        return l
            
