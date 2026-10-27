class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map1 = {}
        map2 = {}
        for ele in s:
            if ele not in map1:
                map1[ele] = 1
            else:
                map1[ele] += 1
        for ele in t:
            if ele not in map2:
                map2[ele] = 1
            else:
                map2[ele] += 1
        if map1 == map2:
            return True
        else:
            return False