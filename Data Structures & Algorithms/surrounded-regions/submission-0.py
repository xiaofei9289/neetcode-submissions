

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])

        def dfs(r, c):
            # 越界
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return

            # 不是 O，就不用继续
            if board[r][c] != "O":
                return

            # 标记为安全区域
            board[r][c] = "T"

            # 上下左右继续 DFS
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # 1. 从左右两条边开始找安全的 O
        for r in range(rows):
            if board[r][0] == "O":
                dfs(r, 0)

            if board[r][cols - 1] == "O":
                dfs(r, cols - 1)

        # 2. 从上下两条边开始找安全的 O
        for c in range(cols):
            if board[0][c] == "O":
                dfs(0, c)

            if board[rows - 1][c] == "O":
                dfs(rows - 1, c)

        # 3. 最后统一处理
        for r in range(rows):
            for c in range(cols):

                # 剩下的 O 都是被包围的
                if board[r][c] == "O":
                    board[r][c] = "X"

                # T 是安全的 O，恢复回来
                elif board[r][c] == "T":
                    board[r][c] = "O"