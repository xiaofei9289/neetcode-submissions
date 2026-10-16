class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        movement = [[0,1],[0,-1],[1,0],[-1,0]]
        queue = deque()
        fresh_fruits = 0
        time = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c))
                elif grid[r][c] == 1:
                    fresh_fruits += 1

        while queue and fresh_fruits>0:
            for i in range(len(queue)):

                r,c = queue.popleft()
                for x, y in movement:
                    new_r = r + x
                    new_c = c + y

                    if (
                            new_r < 0 or
                            new_r >= rows or
                            new_c < 0 or
                            new_c >= cols
                        ):
                            continue

                    if grid[new_r][new_c] != 1:
                            continue

                    grid[new_r][new_c] = 2
                    fresh_fruits -= 1
                    queue.append((new_r, new_c))
            time += 1
        if fresh_fruits == 0:
            return time
        return -1







