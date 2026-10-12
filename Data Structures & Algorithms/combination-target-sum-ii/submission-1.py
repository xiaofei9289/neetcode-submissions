class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtrack(start, path, total):
            if total == target:
                res.append(path.copy())
                return

            for i in range(start, len(candidates)):
                # 同一层去重
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # 剪枝
                if total + candidates[i] > target:
                    break

                # 选择当前数字
                path.append(candidates[i])

                # i + 1：当前元素不能重复使用
                backtrack(i + 1, path, total + candidates[i])

                # 撤销选择
                path.pop()

        backtrack(0, [], 0)

        return res