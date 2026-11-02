class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for ele in strs:
            res = res + str(len(ele)) + "#" + ele 
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        start = 0 
        while start < len(s):
            slid = start
            while s[slid] != "#":
                slid += 1
            cur_length = int(s[start:slid])
            single_word = s[slid+1:slid+1+cur_length]
            res.append(single_word)
            start = slid + 1 + cur_length
        return res

