class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for ele in strs:
            res = res + str(len(ele)) + "#" + ele
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        pointer = 0
        while pointer < len(s):
            j= pointer
            while s[j:j+1] != "#":
                j += 1
            str_len = int(s[pointer:j])
            res.append(s[j+1:j+1+str_len])
            pointer = j + 1 + str_len
        return res

