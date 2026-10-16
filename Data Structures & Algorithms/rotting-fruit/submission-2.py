class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        final_time = 0
        rotten_queue = deque()
        fresh_num = 0
        movement = [[0,1],[0,-1],[1,0],[-1,0]]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh_num += 1
                elif grid[r][c] == 2:
                     rotten_queue.append((r,c))
        
        while rotten_queue and fresh_num>0:
            for i in range(len(rotten_queue)):
                r,c = rotten_queue.popleft()
                for x, y in movement:
                    new_r = x + r
                    new_c = y + c
                    if new_r<0 or new_r>=rows or new_c<0 or new_c >=cols:
                        continue
                    if grid[new_r][new_c] != 1:
                        continue
                    grid[new_r][new_c] = 2
                    fresh_num -= 1
                    rotten_queue.append((new_r,new_c))
            final_time += 1
        if fresh_num == 0:
            return final_time
        return -1
