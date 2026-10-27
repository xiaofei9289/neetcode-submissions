class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for ele in strs:
            res = res + str(len(ele)) + "#" + ele 
        return res



    def decode(self, s: str) -> List[str]:
        res = []
        p = 0
        while p < len(s):
            q = p
            while s[q:q+1] != "#":
                q = q+1
            ele_leng = int(s[p:q])
            res.append(s[q+1: q+1+ele_leng])
            p = q+1+ele_leng
        return res

