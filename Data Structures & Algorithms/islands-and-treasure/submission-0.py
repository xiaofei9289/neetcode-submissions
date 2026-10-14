class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])

        queue = deque()
        INF = 2147483647

        # 1. 把所有宝箱 0 先放进 queue
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c))

        directions = [
            (1, 0),   # 下
            (-1, 0),  # 上
            (0, 1),   # 右
            (0, -1)   # 左
        ]

        # 2. BFS
        while queue:
            r, c = queue.popleft()

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                # 越界
                if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                    continue

                # 只处理还没有访问过的陆地
                if grid[nr][nc] != INF:
                    continue

                # 当前距离 + 1
                grid[nr][nc] = grid[r][c] + 1

                # 放进 queue，之后继续向外扩散
                queue.append((nr, nc))
        