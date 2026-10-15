class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        movements = [(0,1),(0,-1),(1,0),(-1,0)]
        pacific = set()
        atlantic = set()

        def dfs(r,c,visited):
            visited.add((r,c))
            for r_move, c_move in movements:
                new_r = r_move + r
                new_c = c_move + c
                if new_c < 0 or new_r < 0 or new_c >= cols or new_r >=rows:
                    continue
                if (new_r, new_c) in visited:
                    continue
                
                if heights[new_r][new_c] < heights[r][c]:
                    continue
                dfs(new_r, new_c, visited)
        for c in range(cols):
            dfs(0,c,pacific)
        for r in range(rows):
            dfs(r,0,pacific)
        for c in range(cols):
            dfs(rows-1,c,atlantic)
        for r in range(rows):
            dfs(r,cols-1,atlantic)

        res = []
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append([r,c])
        return res

