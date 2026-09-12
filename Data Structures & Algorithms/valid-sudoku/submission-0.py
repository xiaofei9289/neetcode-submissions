class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for raw in range(9):
            seen=set()
            for column in range(9):
                num=board[raw][column]
                if num==".":
                    continue
                elif num in seen:
                    return False
                else:
                    seen.add(num)
        for column in range(9):
            seen=set()
            for raw in range(9):
                num=board[raw][column]
                if num==".":
                    continue
                elif num in seen:
                    return False
                else:
                    seen.add(num)
        for start_row in range(0,9,3):
            for start_column in range(0,9,3):
                seen=set()
                for row in range(start_row,start_row+3):
                    for column in range(start_column,start_column+3):
                        num=board[row][column]
                        if num==".":
                            continue
                        elif num in seen:
                            return False
                        else:
                            seen.add(num)
        return True