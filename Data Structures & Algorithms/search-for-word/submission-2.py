class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        visited = set()
        def backtracking(r,c,i):
            if i == len(word):
                return True
            if min(r,c)<0 or r>=rows or c>=cols:
                return False
            if board[r][c]!=word[i]:
                return False
            if (r,c) in visited:
                return False
            visited.add((r,c))
            found = (
                backtracking(r + 1, c, i + 1) or
                backtracking(r - 1, c, i + 1) or
                backtracking(r, c + 1, i + 1) or
                backtracking(r, c - 1, i + 1)
            )
            visited.remove((r,c))
            return found
        for r in range(rows):
            for c in range(cols):
                if backtracking(r, c, 0):
                    return True
        return False

