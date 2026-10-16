class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        move_step = [(0,1),(0,-1),(1,0),(-1,0)]
        flow_to_pac=set()
        flow_to_atla=set()
        res=[]
        def dfs(r:int,c:int,visited:set):
            visited.add((r,c))
            for x,y in move_step:
                new_r = r + x
                new_c = c + y

                if new_r<0 or new_r>=rows or new_c<0 or new_c>=cols:
                    continue
                if heights[new_r][new_c]<heights[r][c]:
                    continue
                if (new_r,new_c) in visited:
                    continue
                dfs(new_r,new_c,visited)

        for c in range(cols):
            dfs(0,c,flow_to_pac)
        for c in range(cols):
            dfs(rows-1,c,flow_to_atla)
        for r in range(rows):
            dfs(r,0,flow_to_pac)
        for r in range(rows):
            dfs(r,cols-1,flow_to_atla)

        for r in range(rows):
            for c in range(cols):
                if (r,c) in flow_to_atla and (r,c) in flow_to_pac:
                    res.append([r,c])
        return res
