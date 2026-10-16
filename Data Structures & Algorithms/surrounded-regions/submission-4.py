class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        move_step = [[0,1],[0,-1],[1,0],[-1,0]]
        queue = deque()

        for r in range(rows):
            if board[r][0]=="O":
                queue.append((r,0))
                board[r][0]="Temp"
            if board[r][cols-1]=="O":
                queue.append((r,cols-1))
                board[r][cols-1]="Temp"
        for c in range(cols):
            if board[0][c]=="O":
                queue.append((0,c))
                board[0][c]="Temp"
            if board[rows-1][c]=="O":
                queue.append((rows-1,c))
                board[rows-1][c]="Temp"
        while queue:
            r, c = queue.popleft()
            for x, y in move_step:
                new_r = x + r
                new_c = y + c
                if new_r < 0 or new_r >= rows or new_c < 0 or new_c >= cols:
                        continue
                if board[new_r][new_c] != "O":
                    continue
                board[new_r][new_c] = "Temp"
                queue.append((new_r, new_c))
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "Temp":
                    board[r][c] = "O"
            












        