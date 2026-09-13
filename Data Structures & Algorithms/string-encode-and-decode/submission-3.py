class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for ele in strs:
            res += "///"
            res += ele
            
        return res

    def decode(self, s: str) -> List[str]:
        split_s = s.split("///")
        return split_s[1:]


