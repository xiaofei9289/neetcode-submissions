class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        output = []
        move_steps = [[0,1], [0,-1],[1,0],[-1,0]]
        pacific_reached = set()
        atlantic_reached = set()


        def dfs(r:int,c:int,reached:set):
            reached.add((r,c))
            for x,y in move_steps:
                new_r = x + r
                new_c = y + c

                if new_r<0 or new_r>=rows or new_c<0 or new_c>=cols:
                    continue
                if (new_r,new_c) in reached:
                    continue
                if heights[new_r][new_c] < heights[r][c]:
                    continue
                dfs(new_r,new_c,reached)
        for r in range(rows):
            dfs(r,0,pacific_reached)
        for c in range(cols):
            dfs(0,c,pacific_reached)
        for r in range(rows):
            dfs(r,cols-1,atlantic_reached)
        for c in range(cols):
            dfs(rows-1,c,atlantic_reached)
        
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pacific_reached and (r,c) in atlantic_reached:
                    output.append((r,c))
        return output     