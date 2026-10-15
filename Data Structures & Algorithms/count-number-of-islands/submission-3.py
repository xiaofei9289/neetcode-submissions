class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        movement = [[0,1],[0,-1],[1,0],[-1,0]]
        visited = set()
        num_of_islands=0
        def dfs(r,c,visited):
            visited.add((r,c))
            for x, y in movement:
                new_r = x + r
                new_c = y + c
                if new_r<0 or new_r>=rows or new_c<0 or new_c>=cols:
                    continue
                if (new_r,new_c) in visited:
                    continue
                if grid[new_r][new_c]=="0":
                    continue
                dfs(new_r,new_c,visited)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and (r,c) not in visited:
                    num_of_islands+=1
                    dfs(r,c,visited)
        return num_of_islands
            