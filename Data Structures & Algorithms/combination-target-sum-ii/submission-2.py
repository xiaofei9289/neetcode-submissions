class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtracking(start_index, path, sum):
            if sum == target:
                res.append(path.copy())
                return 
            if sum > target:
                return
            for i in range(start_index,len(candidates)):
                if i>start_index and candidates[i] == candidates[i-1]:
                    continue
                path.append(candidates[i])
                backtracking(i+1, path, candidates[i]+sum)
                path.pop()
        backtracking(0,[],0)
        return res