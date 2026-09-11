class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        res=""
        for element in strs:
            res+=str(len(element))+"#"+element
        return res

        

    def decode(self, s: str) -> List[str]:
        res=[]
        i=0
        while i < len(s):
            j=i
            while s[j]!="#":
                j+=1
            length=int(s[i:j])
            start=j+1
            end=start+length
            res.append(s[start:end])
            i=end
        return res



