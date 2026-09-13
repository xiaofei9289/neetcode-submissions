class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group= {}
        for ele in strs:
            key = "".join(sorted(ele))
            if key in group:
                group[key].append(ele)
            else:
                group[key]=[ele]
        return list(group.values())
        