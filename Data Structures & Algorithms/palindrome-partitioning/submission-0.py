class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def backtrack(start, cur):
            if start == len(s):
                res.append(cur.copy())
                return
            for end in range(start,len(s)):
                substring = s[start:end+1]
                if substring!=substring[::-1]:
                    continue
                cur.append(substring)
                backtrack(end+1,cur)
                cur.pop()
        backtrack(0,[])
        return res