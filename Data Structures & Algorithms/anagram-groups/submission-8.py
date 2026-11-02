class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map ={}
        for ele in strs:
            sorted_ele = tuple(sorted(ele))
            if sorted_ele in map:
                map[sorted_ele].append(ele)
            else:
                map[sorted_ele] = [ele]
        return list(map.values())