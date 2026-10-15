class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        treasure_queue = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==0:
                    treasure_queue.append((r,c))
        movement=[[0,1],[0,-1],[1,0],[-1,0]]     

        while treasure_queue:
            r,c=treasure_queue.popleft()
            for x,y in movement:
                new_r = r+x
                new_c = c+y

                if new_r < 0 or new_r >= rows or new_c < 0 or new_c >= cols:
                    continue
                if grid[new_r][new_c] != 2147483647:
                    continue
                grid[new_r][new_c]=grid[r][c]+1
                treasure_queue.append((new_r,new_c))