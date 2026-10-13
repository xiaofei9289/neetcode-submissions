class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        fianl_result = []
        sorted_candidates = sorted(candidates)
        def backtracking(start_index, path, sum):
            if sum == target:
                fianl_result.append(path.copy())
            if sum > target or start_index >= len(sorted_candidates):
                return
            for i in range(start_index, len(sorted_candidates)):
                if i > start_index and sorted_candidates[i] == sorted_candidates[i-1]:
                    continue
                path.append(sorted_candidates[i])
                backtracking(i+1, path, sorted_candidates[i]+sum)
                path.pop()
        backtracking(0,[],0)
        return fianl_result