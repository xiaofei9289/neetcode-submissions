class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store_map = {}
        for ele in strs:
            key = "".join(sorted(ele))
            if key in store_map:
                store_map[key].append(ele)
            else:
                store_map[key] = [ele]
        return list(store_map.values())