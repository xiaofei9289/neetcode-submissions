class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for ele in strs:
            res = res + str(len(ele)) + "#" + ele
        return res 


    def decode(self, s: str) -> List[str]:
        res = []
        start = 0
        for i in range(1,len(s)):
            if i < start:
                continue
            if s[i-1].isdigit() and s[i] == "#":
                length = int(s[start:i])
                res.append(s[i+1:i+1+length])
                start = i + 1 + length
        return res
