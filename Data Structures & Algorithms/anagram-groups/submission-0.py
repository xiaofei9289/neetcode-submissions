class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        for element in strs:
            sorted_element=''.join(sorted(element))
            res[sorted_element].append(element)
        return list(res.values())