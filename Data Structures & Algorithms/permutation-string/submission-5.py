class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left=0
        freq_s1=defaultdict(int)
        for ele in s1:
            freq_s1[ele]+=1
        freq_s2=defaultdict(int)
        for right in range(len(s2)):
            freq_s2[s2[right]]+=1
            while (right-left+1)>len(s1):
                freq_s2[s2[left]]-=1
                if freq_s2[s2[left]]==0:
                    del freq_s2[s2[left]]
                left+=1
            if freq_s2==freq_s1:
                return True
        return False
            

        