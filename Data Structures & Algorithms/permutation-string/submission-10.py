class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)

        if n1>n2:
            return False
        
        target = defaultdict(int)
        window = defaultdict(int)
        for ele in s1:
            target[ele] += 1

        left = 0 
        for right in range(n2):
            char = s2[right]
            window[char] += 1

            if right - left + 1 > n1:
                window[s2[left]] -= 1

                if window[s2[left]] == 0:
                    del window[s2[left]]
                left += 1
            if window == target:
                return True
        return False