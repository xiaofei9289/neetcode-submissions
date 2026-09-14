class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res=[]
        seen=set()
        left=0
        for ele in s:
            if ele in seen:
                temp=len(seen)
                res.append(temp)

                while ele in seen:
                    seen.remove(s[left])
                    left+=1
            
            seen.add(ele)
        res.append(len(seen))
        return max(res)
        