class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        movement = [[0,1],[0,-1],[1,0],[-1,0]]
        num_islands = 0
        has_visited = set()
        def dfs(r:int,c:int,has_visited:set):
            has_visited.add((r,c))
            for x, y in movement:
                new_r = x + r
                new_c = y + c

                if new_r<0 or new_r>=rows or new_c<0 or new_c>=cols:
                    continue
                if (new_r,new_c) in has_visited:
                    continue
                if grid[new_r][new_c]=="0":
                    continue
                dfs(new_r,new_c,has_visited)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and (r,c) not in has_visited:
                    num_islands +=1
                    dfs(r,c,has_visited)
        return num_islands
