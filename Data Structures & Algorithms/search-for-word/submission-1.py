class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        columns = len(board[0])

        def backtracking(row, column, start_index):
            if start_index == len(word):
                return True
            if row<0 or row>=rows or column <0 or column>=columns:
                return False
            if board[row][column]!= word[start_index]:
                return False
            cur = board[row][column]
            board[row][column] = "#"
            found = (
                backtracking(row + 1, column, start_index + 1) or
                backtracking(row - 1, column, start_index + 1) or
                backtracking(row, column + 1, start_index + 1) or
                backtracking(row, column - 1, start_index + 1)
            )
            board[row][column]=cur
            return found
        for r in range(rows):
            for c in range(columns):
                if backtracking(r, c, 0):
                    return True

        return False