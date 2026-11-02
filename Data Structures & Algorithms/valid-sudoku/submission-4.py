class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if not self.checkBox(board):
            return False
        elif not self.chechRow(board):
            return False
        elif not self.checkCols(board):
            return False
        else:
            return True


    def checkBox(self,board):
        for row in range(0,9,3):
            for col in range(0,9,3):
                seen = set()
                for i in range(row,row+3):
                    for j in range(col, col+3):
                        cur = board[i][j]
                        if cur == ".":
                            continue
                        elif cur in seen:
                            return False
                        else:
                            seen.add(cur)
        return True
    
    def chechRow(self,board):
        
        for row in range(9):
            seen = set()         
            for col in range(9):
                cur = board[row][col]
                if cur == ".":
                    continue
                elif cur in seen:
                    return False
                else:
                    seen.add(cur)
        return True
    
    def checkCols(self, board):
        for col in range(9):
            seen = set()
            for row in range(9):
                cur = board[row][col]

                if cur == ".":
                    continue

                elif cur in seen:
                    return False

                else:
                    seen.add(cur)

        return True


        