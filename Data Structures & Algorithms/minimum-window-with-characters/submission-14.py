class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n1 = len(s)
        n2 = len(t)

        if n2 > n1:
            return ""
        
        minimum_ele = defaultdict(int)
        window_ele = defaultdict(int)

        lef = 0
        min_length = float("inf")
        start = 0

        for ele in t:
            minimum_ele[ele] += 1
        
        for rig in range(n1):
            ele = s[rig]
            window_ele[ele] += 1
            while self.valid(minimum_ele,window_ele):
                cur_win_len = rig - lef + 1
                if cur_win_len < min_length:
                    min_length = cur_win_len
                    start = lef
                window_ele[s[lef]] -= 1
                lef += 1
        if min_length == float("inf"):
            return ""
        return s[start:start + min_length]


    def valid(self, minimum_ele,window_ele):
        for ele in minimum_ele:
            if window_ele[ele]<minimum_ele[ele]:
                return False
        return True
