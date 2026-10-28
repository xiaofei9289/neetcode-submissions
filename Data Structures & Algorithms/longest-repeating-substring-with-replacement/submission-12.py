class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_length = 1
        map = defaultdict(int)
        max_freq = 1

        for right in range(len(s)):
            ele = s[right]
            map[ele] += 1
            max_freq = max(max_freq, map[ele])
            window_lenght = right - left + 1
            while window_lenght - max_freq>k:
                map[s[left]] -= 1
                left += 1
                window_lenght = right - left + 1
            max_length = max(max_length, right-left+1)
        return max_length