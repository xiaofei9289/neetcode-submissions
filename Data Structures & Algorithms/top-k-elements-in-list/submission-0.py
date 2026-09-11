class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        fre_dict={}
        for i in nums:
            if i in fre_dict:
                fre_dict[i]+=1
            else:
                fre_dict[i]=1
        sorted_freq=sorted(fre_dict, key=fre_dict.get,reverse=True)
        res=[]
        for m in range(k):
            res.append(sorted_freq[m])
        return res

