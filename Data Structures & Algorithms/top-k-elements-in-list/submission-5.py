class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for ele in nums:
            if ele in map:
                map[ele] += 1
            else:
                map[ele] = 1
        res =sorted(map, key = lambda a:map[a], reverse=True)
        return res[:k]