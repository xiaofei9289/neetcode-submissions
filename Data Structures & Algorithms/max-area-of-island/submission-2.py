class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        area_of_islands = []
        is_visited=set()
        movements = [[0,1],[0,-1],[1,0],[-1,0]]
        def dfs(r,c,is_visited):
            area = 1
            is_visited.add((r,c))
            for x,y in movements:
                new_r = x + r
                new_c = y + c

                if new_r<0 or new_r >= rows or new_c<0 or new_c>=cols:
                    continue
                if (new_r,new_c) in is_visited:
                    continue
                if grid[new_r][new_c]==0:
                    continue
                area += dfs(new_r,new_c,is_visited)
            return area
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c)not in is_visited:
                    area = dfs(r,c,is_visited)
                    area_of_islands.append(area)
        if not area_of_islands:
            return 0
        return max(area_of_islands)