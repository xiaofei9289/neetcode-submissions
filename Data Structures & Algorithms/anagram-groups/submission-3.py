class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        map = {}


        for ele in strs:
            key = tuple(sorted(ele))
            if key not in map:
                map[key] = []
        
            map[key].append(ele)
        
        for ele in map:
            res.append(map[ele])
        return res

