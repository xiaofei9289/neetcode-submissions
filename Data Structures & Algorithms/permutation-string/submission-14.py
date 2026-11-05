class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        map1 = defaultdict(int)
        map2 = defaultdict(int)

        for ele in s1:
            map1[ele] += 1

        lef = 0
        for rig in range(len(s2)):
            ele = s2[rig]
            map2[ele] += 1
            if rig - lef + 1 > len(s1):
                map2[s2[lef]] -= 1
                if map2[s2[lef]] == 0:
                    del map2[s2[lef]]
                lef += 1
            if map2 == map1:
                return True
        return False
