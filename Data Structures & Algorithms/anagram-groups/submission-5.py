class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        map = {}
        for ele in strs:
            key = tuple(sorted(ele))
            if key in map:
                map[key].append(ele)
            else:
                map[key] = [ele]
        return list(map.values()) 
