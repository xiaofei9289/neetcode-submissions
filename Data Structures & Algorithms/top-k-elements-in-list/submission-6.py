class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map_store = defaultdict(int)

        for ele in nums:
            map_store[ele] += 1
        res = sorted(map_store,key = lambda a: map_store[a], reverse= True)

        return res[:k]
        