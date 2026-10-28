class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        map = defaultdict(int)
        res = 0
        max_freq = 0 

        for right in range(len(s)):
            char = s[right]
            map[char] += 1

            max_freq = max(max_freq, map[char])
            win_leng = right-left+1
            if win_leng - max_freq>k:
                map[s[left]] -= 1
                left +=1
            res = max(res, right-left+1)
        return res


