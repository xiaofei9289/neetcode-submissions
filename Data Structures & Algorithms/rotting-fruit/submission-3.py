class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        fresh_num = 0
        rotten = deque()
        time = 0
        movement = [[0,1],[0,-1],[1,0],[-1,0]]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    rotten.append((r,c))
                if grid[r][c]==1:
                    fresh_num+=1
        while rotten and fresh_num>0:
            for i in range(len(rotten)):
                r,c=rotten.popleft()
                for x, y in movement:
                    new_r = x + r
                    new_c = y + c
                    if new_r<0 or new_r>=rows or new_c<0 or new_c >=cols:
                        continue
                    if grid[new_r][new_c]!=1:
                        continue
                    grid[new_r][new_c]=2
                    fresh_num-=1
                    rotten.append((new_r,new_c))
            time += 1
        if fresh_num==0:
            return time
        return -1














