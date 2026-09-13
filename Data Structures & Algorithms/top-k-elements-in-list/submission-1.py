class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        fre_dict = {}
        for ele in nums:
            if ele in fre_dict:
                fre_dict[ele] += 1
            else:
                fre_dict[ele] = 1
        sorted_nums = sorted(
            fre_dict,
            key = fre_dict.get,
            reverse = True
            )
        return sorted_nums[:k]
