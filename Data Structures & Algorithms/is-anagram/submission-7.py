class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        store_map = {}
        store_map2={}
        for ele in s:
            if ele in store_map.keys():
                store_map[ele]+=1
            else:
                store_map[ele] = 1
        for ele in t:
            if ele in store_map2.keys():
                store_map2[ele]+=1
            else:
                store_map2[ele] = 1
        
        if store_map == store_map2:
            return True
        else:
            return False