class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        pacific = set()
        atlantic = set()
        directions = [
            (1, 0),   
            (-1, 0),  
            (0, 1),   
            (0, -1)   
        ]

        def dfs(r,c,visited):
            visited.add((r, c))
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                # 1. 越界
                if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                    continue

                # 2. 已经访问过
                if (nr, nc) in visited:
                    continue

                # 3. 反向搜索：
                
                if heights[nr][nc] < heights[r][c]:
                    continue

                dfs(nr, nc, visited)

        # Pacific：上边界 + 左边界
        for c in range(cols):
            dfs(0, c, pacific)

        for r in range(rows):
            dfs(r, 0, pacific)

        # Atlantic：下边界 + 右边界
        for c in range(cols):
            dfs(rows - 1, c, atlantic)

        for r in range(rows):
            dfs(r, cols - 1, atlantic)

        # 同时能流到两个海洋
        result = []

        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific and (r, c) in atlantic:
                    result.append([r, c])

        return result