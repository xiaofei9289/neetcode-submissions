class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_len = len(s)
        t_len = len(t)

        if t_len> s_len:
            return ""
        
        needed = defaultdict(int)
        window_covered = defaultdict(int)
        for ele in t:
            needed[ele] += 1
        lef = 0
        min_length = float("inf")
        start = 0

        for rig in range(s_len):
            ele = s[rig]
            window_covered[ele] += 1
            while self.is_covered(needed, window_covered):
                cur_win_length = rig - lef + 1
                if cur_win_length < min_length:
                    min_length = cur_win_length
                    start = lef
                window_covered[s[lef]] -= 1
                lef += 1
        if min_length == float("inf"):
            return ""
        return s[start:start+min_length]

    



    def is_covered(self, less: dict, more:dict):
        for ele in less:
            if less[ele] > more[ele]:
                return False
        return True