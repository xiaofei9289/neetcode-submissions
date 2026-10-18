class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False

        adj_table = defaultdict(list)

        for a, b in edges:
            adj_table[a].append(b)
            adj_table[b].append(a)
        
        queue = deque([0])
        visited= set([0])

        while queue:
            cur_node = queue.popleft()

            for next_node in adj_table[cur_node]:
                if next_node in visited:
                    continue

                visited.add(next_node)
                queue.append(next_node)

        return len(visited) == n