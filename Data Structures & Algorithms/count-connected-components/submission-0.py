class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_table = defaultdict(list)
        for a, b in edges:
            adj_table[a].append(b)
            adj_table[b].append(a)

        visited = set()
        count = 0

        for i in range(n):
            if i in visited:
                continue

            count += 1

            queue = deque([i])
            visited.add(i)

            while queue:
                cur_node = queue.popleft()

                for next_node in adj_table[cur_node]:
                    if next_node in visited:
                        continue

                    visited.add(next_node)
                    queue.append(next_node)

        return count