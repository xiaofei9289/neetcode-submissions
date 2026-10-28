class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        map = defaultdict(int)
        for ele in s1:
            map[ele] += 1
        
        n= len(s1)
        for i in range(len(s2)-n+1):
            temp = map.copy()
            for j in range(i,i+n):
                if s2[j] in temp:
                    temp[s2[j]] -= 1
                else:
                    break
            if all(value == 0 for value in temp.values()):
                return True
        return False


