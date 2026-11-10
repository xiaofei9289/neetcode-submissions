class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    
        n = len(temperatures) 
        res = [0] * n

        store_index = []

        for i in range(n):
            while store_index and temperatures[i] > temperatures[store_index[-1]]:
                prev = store_index.pop()
                res[prev] = i - prev
            store_index.append(i)
        return res
