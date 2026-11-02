class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map1= defaultdict(int)
        for ele in s:
            map1[ele] += 1

        map2 = defaultdict(int)
        for ele in t:
            map2[ele] += 1
        
        if map1 == map2:
            return True
        else:
            return False