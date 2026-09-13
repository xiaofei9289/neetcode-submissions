class Solution:

    def encode(self, strs: List[str]) -> str:
        res = "" 
        for ele in strs:
            res += str(len(ele))
            res += "#"
            res += ele
        return res


    def decode(self, s: str) -> List[str]:
        res = []
        p1 = 0

        while p1 < len(s):
            p2 = p1
            while s[p2] != "#":
                p2 += 1
            string_length = int(s[p1:p2])

            p1 = p2 + 1
            p2 = string_length + p1
            res.append(s[p1:p2])
            p1 = p2
        return res





