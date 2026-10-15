class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])

        def dfs(r_coordinate, c_ordinate):
            if r_coordinate<0 or r_coordinate>=rows or c_ordinate<0 or c_ordinate>=cols:
                return
            if board[r_coordinate][c_ordinate]!="O":
                return
            board[r_coordinate][c_ordinate] = "Safe"

            dfs(r_coordinate+1,c_ordinate)
            dfs(r_coordinate-1,c_ordinate)
            dfs(r_coordinate,c_ordinate+1)
            dfs(r_coordinate,c_ordinate-1)

        for r in range(rows):
            if board[r][0]=="O":
                dfs(r,0)
            if board[r][cols-1]=="O":
                dfs(r,cols-1)
        for c in range(cols):
            if board[0][c]=="O":
                dfs(0,c)
            if board[rows-1][c]=="O":
                dfs(rows-1,c)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] =="O":
                    board[r][c]="X"
                elif board[r][c] == "Safe":
                    board[r][c] = "O"
