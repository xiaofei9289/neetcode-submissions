class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        final_res = []
        sorted_candidates = sorted(candidates)
        
        def backtracking(start_index, path, total):
            if total == target:
                final_res.append(path.copy())
            if start_index >= len(sorted_candidates) or target<total:
                return
            for i in range(start_index,len(sorted_candidates)):
                if i>start_index and sorted_candidates[i] == sorted_candidates[i-1]:
                    continue
                path.append(sorted_candidates[i])
                backtracking(i+1, path, sorted_candidates[i]+total)
                path.pop()
        backtracking(0,[],0)
        return final_res