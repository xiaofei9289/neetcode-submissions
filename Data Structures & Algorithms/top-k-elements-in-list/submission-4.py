class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for ele in nums:
            if ele in map.keys():
                map[ele] += 1
            else:
                map[ele] = 1
        
        sorted_nums = sorted(
            map,
            key = map.get,
            reverse= True
        )
        return sorted_nums[:k]