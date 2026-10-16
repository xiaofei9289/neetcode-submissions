class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        move_step = [[0,1],[0,-1],[1,0],[-1,0]]
        output=set()

        def dfs(r:int, c:int, reached:set):
            if board[r][c] != "O":
                return
            if (r, c) in reached:
                return
            reached.add((r,c))
            board[r][c] = "Temp"
            for x, y in move_step:
                new_r = x + r
                new_c = y + c

                if new_r<0 or new_r>=rows or new_c<0 or new_c>=cols:
                    continue
                if board[new_r][new_c] !="O":
                    continue
                if (new_r,new_c) in reached:
                    continue

                dfs(new_r,new_c,reached)
        for r in range(rows):
            dfs(r,0,output)
        for c in range(cols):
            dfs(0,c,output)
        for r in range(rows):
            dfs(r,cols-1,output)
        for c in range(cols):
            dfs(rows-1,c,output)

        for r in range(rows):
            for c in range(cols):
                if board[r][c]=="O":
                    board[r][c] = "X"
                elif board[r][c]=="Temp":
                    board[r][c] = "O"
        

        