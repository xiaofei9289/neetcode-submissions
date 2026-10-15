class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        move_forward = [(0,1),(0,-1),(1,0),(-1,0)]
        pac_boundary = set()
        alt_boundary = set()

        def dfs(r_coordinate, c_coordinate,is_visited):
            is_visited.add((r_coordinate,c_coordinate))
            for r_move, c_move in move_forward:
                new_r = r_move + r_coordinate
                new_c = c_move + c_coordinate
                if not (0 <= new_r < rows and 0 <= new_c < cols):
                    continue
                if (new_r, new_c) in is_visited:
                    continue
                if heights[new_r][new_c] < heights[r_coordinate][c_coordinate]:
                    continue

                dfs(new_r, new_c, is_visited)
        for c in range(cols):
            dfs(0,c,pac_boundary)
        for r in range(rows):
            dfs(r,0,pac_boundary)
        for c in range(cols):
            dfs(rows-1,c,alt_boundary)
        for r in range(rows):
            dfs(r,cols-1,alt_boundary)
        fianl_res = []

        for r in range(rows):
            for c in range(cols):
                if (r,c) in pac_boundary and (r,c) in alt_boundary:
                    fianl_res.append([r,c])
        return fianl_res