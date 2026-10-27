class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        map ={}
        for ele in strs:
            key = tuple(sorted(ele))
            if key in map:
                map[key].append(ele)
            else:
                map[key] = [ele]
        
        res = list(map.values())
        return res