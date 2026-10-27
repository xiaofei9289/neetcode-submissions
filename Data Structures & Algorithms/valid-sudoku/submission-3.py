class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in range(9):
            row = board[r]
            if not self.isValid(row):
                return False
        for c in range(9):
            col = []
            for r in range(9):
                col.append(board[r][c])
            if not self.isValid(col):
                return False
        for s_r in range(0,9,3):
            for s_c in range(0,9,3):
                square = []
                for r in range(s_r,s_r+3):
                    for c in range(s_c,s_c+3):
                        square.append(board[r][c])
                if not self.isValid(square):
                    return False
        return True

    def isValid(self, nums):
        seen = set()
        for ele in nums:
            if ele == ".":
                continue
            if ele in seen:
                return False
            seen.add(ele)
        return True